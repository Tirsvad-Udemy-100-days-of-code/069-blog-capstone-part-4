[English](Step-2-Log-In-Users) · **Dansk** · [Bahasa Malaysia](Step-2-Log-In-Users-ms)

# Trin 2: Log registrerede brugere ind

## Hvad lektionen bad om

Lad registrerede brugere logge ind på `/login` med e-mail og adgangskode. Find brugeren med en `where()`-klausul, kontroller adgangskoden og log brugeren ind med Flask-Login.

## Hvad vi byggede

En `LoginForm` og en `/login`-rute. En forkert e-mail eller adgangskode besvares med `flash()`, og brugeren bliver på formularen.

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

## Sådan ser det ud

![Loginformularen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02a-login-form.png)

![En forkert adgangskode vises som flash-besked](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02b-login-wrong-password.png)

## Hvad vi fik ud af det

- `where()` filtrerer en forespørgsel, så én e-mail finder én bruger.
- `check_password_hash()` sammenligner uden at afkode hashen.
- `flash()` giver feedback én gang og afslører ikke mere end nødvendigt.

Forrige trin: [Registrer nye brugere](Step-1-Register-New-Users-da) · Næste trin: [Beskyt ruter](Step-3-Protect-Routes-da) · [Tilbage til oversigten](Home-da)
