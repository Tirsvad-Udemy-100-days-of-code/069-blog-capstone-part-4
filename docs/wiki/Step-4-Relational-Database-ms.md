[English](Step-4-Relational-Database) · [Dansk](Step-4-Relational-Database-da) · **Bahasa Malaysia**

# Langkah 4: Cipta pangkalan data hubungan

## Apa yang diminta dalam kuliah

Kaitkan setiap catatan blog dengan penulisnya. Buat hubungan satu-ke-banyak dua hala antara `User` (induk) dan `BlogPost` (anak), cipta semula pangkalan data kerana skema berubah, dan tunjukkan nama penulis daripada objek `User`.

## Apa yang kami bina

Kunci asing `author_id` pada `blog_posts`, `relationship()` dengan `back_populates` pada kedua-dua belah, dan `blog.db` yang baharu. Templat menggunakan `post.author.name`.

```python
class User(UserMixin, db.Model):
    __tablename__ = "users"
    posts = relationship("BlogPost", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
```

## Rupanya

![Cipta pangkalan data hubungan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-04-relational-schema.png)

Imej ini ialah ilustrasi dengan data contoh, dilukis untuk repositori ini; ia bukan tangkapan skrin projek kursus.

## Apa yang kami perolehi

- Kunci asing berada pada jadual anak; `relationship()` memberi sisi Python baginya.
- `back_populates` menjadikan hubungan berfungsi dua hala.
- Perubahan skema memerlukan migrasi; jika tiada data yang perlu disimpan, mencipta semula pangkalan data sudah memadai.

Langkah sebelumnya: [Lindungi laluan](Step-3-Protect-Routes-ms) · Langkah seterusnya: [Komen](Step-5-Comments-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
