[English](Step-1-Register-New-Users) · [Dansk](Step-1-Register-New-Users-da) · **Bahasa Malaysia**

# Langkah 1: Daftarkan pengguna baharu

## Apa yang diminta dalam kuliah

Benarkan orang mendaftar di `/register`. Buat `RegisterForm`, jadual `User`, cincang dan garamkan kata laluan dengan Werkzeug, dan paparkan borang dengan Bootstrap-Flask. Jangan risau tentang Flask-Login dahulu, kemudian tambah satu baris supaya pengguna baharu log masuk dan dibawa ke laman utama.

## Apa yang kami bina

`RegisterForm`, jadual `users` dan laluan `/register` yang menyimpan kata laluan yang dicincang dan digaram. `login_user()` dipanggil sebaik sahaja pengguna disimpan.

```python
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")

hashed = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
new_user = User(email=form.email.data, name=form.name.data, password=hashed)
db.session.add(new_user)
db.session.commit()
login_user(new_user)
return redirect(url_for("get_all_posts"))
```

## Rupanya

![Daftarkan pengguna baharu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-01-register-form.png)

Imej ini ialah ilustrasi dengan data contoh, dilukis untuk repositori ini; ia bukan tangkapan skrin projek kursus.

## Apa yang kami perolehi

- Kelas borang menerangkan medan dan pengesahan sekali sahaja; `render_form()` melukisnya.
- Jangan simpan kata laluan: simpan cincang bergaram.
- Log masuk pengguna sebaik sahaja mendaftar menjimatkan satu borang lagi.

Langkah seterusnya: [Log masuk pengguna](Step-2-Log-In-Users-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
