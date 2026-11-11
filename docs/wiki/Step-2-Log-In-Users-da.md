[English](Step-2-Log-In-Users) · **Dansk** · [Bahasa Malaysia](Step-2-Log-In-Users-ms)

# Trin 2: Log registrerede brugere ind

## Hvad lektionen bad om

Lad registrerede brugere logge ind på `/login` med e-mail og adgangskode. Find brugeren med en `where()`-klausul, kontroller adgangskoden og log brugeren ind med Flask-Login.

## Hvad vi byggede

En `LoginForm` og en `/login`-rute. En forkert e-mail eller adgangskode besvares med `flash()`, og brugeren bliver på formularen.

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

## Sådan ser det ud

![Log registrerede brugere ind](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-02-login-form.png)

Billedet er en illustration med eksempeldata, tegnet til dette repository; det er ikke et screenshot af kursets projekt.

## Hvad vi fik ud af det

- `where()` filtrerer en forespørgsel, så én e-mail finder én bruger.
- `check_password_hash()` sammenligner uden at afkode hashen.
- `flash()` giver feedback én gang og afslører ikke mere end nødvendigt.

Forrige trin: [Registrer nye brugere](Step-1-Register-New-Users-da) · Næste trin: [Beskyt ruter](Step-3-Protect-Routes-da) · [Tilbage til oversigten](Home-da)
