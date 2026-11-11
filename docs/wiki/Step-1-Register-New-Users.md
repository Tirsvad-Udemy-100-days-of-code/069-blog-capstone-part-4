**English** · [Dansk](Step-1-Register-New-Users-da) · [Bahasa Malaysia](Step-1-Register-New-Users-ms)

# Step 1: Register new users

## What the lecture asked

Let people sign up at `/register`. Create a `RegisterForm`, a `User` table, hash and salt the password with Werkzeug, and render the form with Bootstrap-Flask. Do not worry about Flask-Login yet, then add one line so a new user is logged in and sent home.

## What we built

A `RegisterForm`, a `users` table and a `/register` route that stores a hashed and salted password. `login_user()` is called right after the user is saved.

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

## What it looks like

![Register new users](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-01-register-form.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- A form class describes the fields and validation once; `render_form()` draws it.
- Never store a password: store the salted hash.
- Logging the user in right after registering saves a second form.

Next step: [Log in registered users](Step-2-Log-In-Users) · [Back to the overview](Home)
