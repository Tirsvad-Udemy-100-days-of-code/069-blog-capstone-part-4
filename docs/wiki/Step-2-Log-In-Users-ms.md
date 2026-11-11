[English](Step-2-Log-In-Users) · [Dansk](Step-2-Log-In-Users-da) · **Bahasa Malaysia**

# Langkah 2: Log masuk pengguna berdaftar

## Apa yang diminta dalam kuliah

Benarkan pengguna berdaftar log masuk di `/login` dengan e-mel dan kata laluan. Cari pengguna dengan klausa `where()`, semak kata laluan dan log masuk pengguna dengan Flask-Login.

## Apa yang kami bina

`LoginForm` dan laluan `/login`. E-mel atau kata laluan yang salah dijawab dengan `flash()` dan pengguna kekal pada borang.

```python
def login() -> str | Response:
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = current_use_cases().authenticate_user.execute(
                form.email.data or "", form.password.data or ""
            )
        except UnknownEmailError:
            flash(FLASH_UNKNOWN_EMAIL)
        except InvalidCredentialsError:
            flash(FLASH_WRONG_PASSWORD)
        else:
            login_user(LoginUser(user))
            return redirect(url_for("get_all_posts"))
    ...
```

## Rupanya

![Borang log masuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02a-login-form.png)

![Kata laluan salah dipaparkan sebagai mesej kilat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02b-login-wrong-password.png)

## Apa yang kami perolehi

- `where()` menapis pertanyaan, jadi satu e-mel menemui satu pengguna.
- `check_password_hash()` membandingkan tanpa menyahkod cincang.
- `flash()` memberi maklum balas sekali dan tidak mendedahkan lebih daripada perlu.

Langkah sebelumnya: [Daftar pengguna baharu](Step-1-Register-New-Users-ms) · Langkah seterusnya: [Lindungi laluan](Step-3-Protect-Routes-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
