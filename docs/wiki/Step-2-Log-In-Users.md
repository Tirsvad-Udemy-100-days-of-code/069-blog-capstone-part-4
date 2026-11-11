**English** · [Dansk](Step-2-Log-In-Users-da) · [Bahasa Malaysia](Step-2-Log-In-Users-ms)

# Step 2: Log in registered users

## What the lecture asked

Let registered users log in at `/login` with their email and password. Look the user up with a `where()` clause, check the password and log them in with Flask-Login.

## What we built

A `LoginForm` and a `/login` route. A wrong email or a wrong password is answered with `flash()` and the user stays on the form.

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

## What it looks like

![The login form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02a-login-form.png)

![A wrong password is flashed](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02b-login-wrong-password.png)

## What we gained

- `where()` filters a query, so one email finds one user.
- `check_password_hash()` compares without decoding the hash.
- `flash()` gives feedback once and does not reveal more than needed.

Previous step: [Register new users](Step-1-Register-New-Users) · Next step: [Protect routes](Step-3-Protect-Routes) · [Back to the overview](Home)
