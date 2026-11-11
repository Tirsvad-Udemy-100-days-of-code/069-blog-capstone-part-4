**English** · [Dansk](Step-2-Log-In-Users-da) · [Bahasa Malaysia](Step-2-Log-In-Users-ms)

# Step 2: Log in registered users

## What the lecture asked

Let registered users log in at `/login` with their email and password. Look the user up with a `where()` clause, check the password and log them in with Flask-Login.

## What we built

A `LoginForm` and a `/login` route. A wrong email or a wrong password is answered with `flash()` and the user stays on the form.

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

## What it looks like

![Log in registered users](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02-login-form.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- `where()` filters a query, so one email finds one user.
- `check_password_hash()` compares without decoding the hash.
- `flash()` gives feedback once and does not reveal more than needed.

Previous step: [Register new users](Step-1-Register-New-Users) · Next step: [Protect routes](Step-3-Protect-Routes) · [Back to the overview](Home)
