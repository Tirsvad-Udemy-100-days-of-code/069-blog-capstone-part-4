[English](Step-5-Comments) · **Dansk** · [Bahasa Malaysia](Step-5-Comments-ms)

# Trin 5: Lad alle brugere skrive kommentarer

## Hvad lektionen bad om

Lad indloggede brugere kommentere indlæg. Tilføj en `CommentForm` med et CKEditor-felt, en `Comment`-tabel knyttet til både `User` og `BlogPost`, tag kun imod kommentarer fra indloggede brugere, og vis alle kommentarer på indlægssiden.

## Hvad vi byggede

En `comments`-tabel med to fremmednøgler (`author_id` og `post_id`), relationer på `User` og `BlogPost` og en `/post/<int:post_id>`-rute, der accepterer `GET` og `POST`. Anonyme brugere får en besked og sendes til `/login`.

```python
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
```

## Sådan ser det ud

![Lad alle brugere skrive kommentarer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05a-comment-form.png)

![Lad alle brugere skrive kommentarer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05b-comments-list.png)

Billedet er en illustration med eksempeldata, tegnet til dette repository; det er ikke et screenshot af kursets projekt.

## Hvad vi fik ud af det

- En-til-mange-relationer kan kædes sammen: bruger til indlæg, bruger til kommentarer, indlæg til kommentarer.
- En rute, der gemmer data, skal bruge `POST`.
- CKEditor gemmer HTML, så skabelonen markerer det som sikkert at vise.

Forrige trin: [Relationel database](Step-4-Relational-Database-da) · Næste trin: [Gravatar-billeder](Step-6-Gravatar-da) · [Tilbage til oversigten](Home-da)
