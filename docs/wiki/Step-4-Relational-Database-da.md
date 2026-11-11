[English](Step-4-Relational-Database) · **Dansk** · [Bahasa Malaysia](Step-4-Relational-Database-ms)

# Trin 4: Opret en relationel database

## Hvad lektionen bad om

Knyt hvert blogindlæg til sin forfatter. Lav en tovejs en-til-mange-relation mellem `User` (forælder) og `BlogPost` (barn), opret databasen igen fordi skemaet er ændret, og vis forfatterens navn fra `User`-objektet.

## Hvad vi byggede

En fremmednøgle `author_id` på `blog_posts`, `relationship()` med `back_populates` på begge sider og en ny `blog.db`. Skabelonerne bruger `post.author.name`.

```python
class User(UserMixin, db.Model):
    __tablename__ = "users"
    posts = relationship("BlogPost", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
```

## Sådan ser det ud

![Opret en relationel database](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-04-relational-schema.png)

Billedet er en illustration med eksempeldata, tegnet til dette repository; det er ikke et screenshot af kursets projekt.

## Hvad vi fik ud af det

- En fremmednøgle ligger i barnetabellen; `relationship()` giver Python-siden af den.
- `back_populates` får relationen til at virke i begge retninger.
- En skemaændring kræver en migrering; uden data, der er værd at beholde, er det nok at oprette databasen igen.

Forrige trin: [Beskyt ruter](Step-3-Protect-Routes-da) · Næste trin: [Kommentarer](Step-5-Comments-da) · [Tilbage til oversigten](Home-da)
