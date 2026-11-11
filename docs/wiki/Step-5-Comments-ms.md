[English](Step-5-Comments) · [Dansk](Step-5-Comments-da) · **Bahasa Malaysia**

# Langkah 5: Benarkan mana-mana pengguna menambah komen

## Apa yang diminta dalam kuliah

Benarkan pengguna yang log masuk memberi komen pada catatan. Tambah `CommentForm` dengan medan CKEditor, jadual `Comment` yang berkait dengan `User` dan `BlogPost`, terima komen hanya daripada pengguna yang log masuk, dan tunjukkan semua komen pada halaman catatan.

## Apa yang kami bina

Jadual `comments` dengan dua kunci asing (`author_id` dan `post_id`), hubungan pada `User` dan `BlogPost`, dan laluan `/post/<int:post_id>` yang menerima `GET` dan `POST`. Pengguna tanpa log masuk diberi mesej dan dialihkan ke `/login`.

```python
class CommentModel(Base):
    __tablename__ = "comments"
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    comment_author: Mapped[UserModel] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"), nullable=False)
    parent_post: Mapped[PostModel] = relationship(back_populates="comments")
```

## Rupanya

![Borang komen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05a-comment-form.png)

![Komen tanpa log masuk: mesej kilat dan alih ke log masuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05b-comment-login-required.png)

![Komen dengan avatar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-05c-comments-list.png)

## Apa yang kami perolehi

- Hubungan satu-ke-banyak boleh dirantai: pengguna ke catatan, pengguna ke komen, catatan ke komen.
- Laluan yang menyimpan data memerlukan kaedah `POST`.
- CKEditor menyimpan HTML, jadi templat menandakannya selamat untuk dipaparkan.

Langkah sebelumnya: [Pangkalan data hubungan](Step-4-Relational-Database-ms) · Langkah seterusnya: [Gambar Gravatar](Step-6-Gravatar-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
