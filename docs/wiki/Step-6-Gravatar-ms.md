[English](Step-6-Gravatar) · [Dansk](Step-6-Gravatar-da) · **Bahasa Malaysia**

# Langkah 6: Tambah gambar profil Gravatar

## Apa yang diminta dalam kuliah

Tunjukkan gambar profil di sebelah setiap komen. Pakej `flask-gravatar` tidak lagi diselenggara, jadi bina sendiri URL Gravatar daripada cincang alamat e-mel.

## Apa yang kami bina

Pembantu kecil yang menukar e-mel kepada huruf kecil, mencincangnya dan memulangkan URL gambar. `post.html` menunjukkannya di sebelah setiap komen.

```python
def gravatar_url(email, size=100):
    digest = hashlib.sha256(email.strip().lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d=retro&r=g"
```

## Rupanya

![Tambah gambar profil Gravatar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-06-gravatar.png)

Imej ini ialah ilustrasi dengan data contoh, dilukis untuk repositori ini; ia bukan tangkapan skrin projek kursus.

## Apa yang kami perolehi

- Gravatar hanya memerlukan cincang e-mel, tanpa akaun di pihak kami.
- Pakej yang tidak diselenggara boleh diganti dengan beberapa baris.
- Imej lalai (`d=retro`) meliputi orang tanpa Gravatar.

Langkah sebelumnya: [Komen](Step-5-Comments-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
