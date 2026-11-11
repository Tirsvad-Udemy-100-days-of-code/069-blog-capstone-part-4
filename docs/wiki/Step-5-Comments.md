**English** · [Dansk](Step-5-Comments-da) · [Bahasa Malaysia](Step-5-Comments-ms)

# Step 5: Allow any user to add comments

## What the lecture asked

Let logged-in users comment on posts. Add a `CommentForm` with a CKEditor field, a `Comment` table related to both `User` and `BlogPost`, only accept comments from logged-in users, and show all comments on the post page.

## What we built

A `comments` table with two foreign keys (`author_id` and `post_id`), relationships on `User` and `BlogPost`, and a `/post/<int:post_id>` route that accepts `GET` and `POST`. Anonymous users are flashed a message and redirected to `/login`.

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

## What it looks like

![Allow any user to add comments](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05a-comment-form.png)

![Allow any user to add comments](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05b-comments-list.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- One-to-many relationships can be chained: user to posts, user to comments, post to comments.
- A route that saves data needs the `POST` method.
- CKEditor saves HTML, so the template marks it safe to render.

Previous step: [Relational database](Step-4-Relational-Database) · Next step: [Gravatar pictures](Step-6-Gravatar) · [Back to the overview](Home)
