**English** · [Dansk](Step-5-Comments-da) · [Bahasa Malaysia](Step-5-Comments-ms)

# Step 5: Allow any user to add comments

## What the lecture asked

Let logged-in users comment on posts. Add a `CommentForm` with a CKEditor field, a `Comment` table related to both `User` and `BlogPost`, only accept comments from logged-in users, and show all comments on the post page.

## What we built

A `comments` table with two foreign keys (`author_id` and `post_id`), relationships on `User` and `BlogPost`, and a `/post/<int:post_id>` route that accepts `GET` and `POST`. Anonymous users are flashed a message and redirected to `/login`.

```python
class CommentModel(Base):
    __tablename__ = "comments"
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    comment_author: Mapped[UserModel] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"), nullable=False)
    parent_post: Mapped[PostModel] = relationship(back_populates="comments")
```

## What it looks like

![The comment form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05a-comment-form.png)

![Anonymous comment: flash and redirect to login](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05b-comment-login-required.png)

![Comments with avatars](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05c-comments-list.png)

## What we gained

- One-to-many relationships can be chained: user to posts, user to comments, post to comments.
- A route that saves data needs the `POST` method.
- CKEditor saves HTML, so the template marks it safe to render.

Previous step: [Relational database](Step-4-Relational-Database) · Next step: [Gravatar pictures](Step-6-Gravatar) · [Back to the overview](Home)
