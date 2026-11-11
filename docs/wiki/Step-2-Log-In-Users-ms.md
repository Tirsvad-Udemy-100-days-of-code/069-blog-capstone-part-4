[English](Step-2-Log-In-Users) · [Dansk](Step-2-Log-In-Users-da) · **Bahasa Malaysia**

# Langkah 2: Log masuk pengguna berdaftar

## Apa yang diminta dalam kuliah

Benarkan pengguna berdaftar log masuk di `/login` dengan e-mel dan kata laluan. Cari pengguna dengan klausa `where()`, semak kata laluan dan log masuk pengguna dengan Flask-Login.

## Apa yang kami bina

`LoginForm` dan laluan `/login`. E-mel atau kata laluan yang salah dijawab dengan `flash()` dan pengguna kekal pada borang.

```python
user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
if not user:
    flash("That email does not exist, please try again.")
elif not check_password_hash(user.password, form.password.data):
    flash("Password incorrect, please try again.")
else:
    login_user(user)
    return redirect(url_for("get_all_posts"))
```

## Rupanya

![Log masuk pengguna berdaftar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02-login-form.png)

Imej ini ialah ilustrasi dengan data contoh, dilukis untuk repositori ini; ia bukan tangkapan skrin projek kursus.

## Apa yang kami perolehi

- `where()` menapis pertanyaan, jadi satu e-mel menemui satu pengguna.
- `check_password_hash()` membandingkan tanpa menyahkod cincang.
- `flash()` memberi maklum balas sekali dan tidak mendedahkan lebih daripada perlu.

Langkah sebelumnya: [Daftar pengguna baharu](Step-1-Register-New-Users-ms) · Langkah seterusnya: [Lindungi laluan](Step-3-Protect-Routes-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
