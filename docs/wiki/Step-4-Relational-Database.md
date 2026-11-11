**English** · [Dansk](Step-4-Relational-Database-da) · [Bahasa Malaysia](Step-4-Relational-Database-ms)

# Step 4: Create a relational database

## What the lecture asked

Link every blog post to its author. Make a bidirectional one-to-many relationship between `User` (parent) and `BlogPost` (child), recreate the database because the schema changed, and show the author name from the `User` object.

## What we built

A foreign key `author_id` on `blog_posts`, `relationship()` with `back_populates` on both sides, and a fresh `blog.db`. Templates use `post.author.name`.

```python
class User(UserMixin, db.Model):
    __tablename__ = "users"
    posts = relationship("BlogPost", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
```

## What it looks like

![Create a relational database](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-04-relational-schema.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- A foreign key lives on the child table; `relationship()` gives the Python side of it.
- `back_populates` makes the link work in both directions.
- A schema change needs a migration; with no data worth keeping, recreating the database is enough.

Previous step: [Protect routes](Step-3-Protect-Routes) · Next step: [Comments](Step-5-Comments) · [Back to the overview](Home)
