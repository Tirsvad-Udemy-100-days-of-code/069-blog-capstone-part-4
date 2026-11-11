[English](Step-1-Register-New-Users) · [Dansk](Step-1-Register-New-Users-da) · **Bahasa Malaysia**

# Langkah 1: Daftarkan pengguna baharu

## Apa yang diminta dalam kuliah

Benarkan orang mendaftar di `/register`. Buat `RegisterForm`, jadual `User`, cincang dan garamkan kata laluan dengan Werkzeug, dan paparkan borang dengan Bootstrap-Flask. Jangan risau tentang Flask-Login dahulu, kemudian tambah satu baris supaya pengguna baharu log masuk dan dibawa ke laman utama.

## Apa yang kami bina

`RegisterForm`, jadual `users` dan laluan `/register` yang menyimpan kata laluan yang dicincang dan digaram. `login_user()` dipanggil sebaik sahaja pengguna disimpan.

```python
def register() -> str | Response:
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = current_use_cases().register_user.execute(form.to_registration())
        except EmailAlreadyRegisteredError:
            flash(FLASH_ALREADY_REGISTERED)
            return redirect(url_for("login"))
        login_user(LoginUser(user))
        return redirect(url_for("get_all_posts"))
    ...

# infrastructure/password_hasher.py
generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
```

## Rupanya

![Borang pendaftaran](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-01-register-form.png)

## Apa yang kami perolehi

- Kelas borang menerangkan medan dan pengesahan sekali sahaja; `render_form()` melukisnya.
- Jangan simpan kata laluan: simpan cincang bergaram.
- Log masuk pengguna sebaik sahaja mendaftar menjimatkan satu borang lagi.

Langkah seterusnya: [Log masuk pengguna](Step-2-Log-In-Users-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
