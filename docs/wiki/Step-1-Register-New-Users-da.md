[English](Step-1-Register-New-Users) · **Dansk** · [Bahasa Malaysia](Step-1-Register-New-Users-ms)

# Trin 1: Registrer nye brugere

## Hvad lektionen bad om

Lad folk tilmelde sig på `/register`. Lav en `RegisterForm`, en `User`-tabel, hash og salt adgangskoden med Werkzeug, og vis formularen med Bootstrap-Flask. Vent med Flask-Login, og tilføj så én linje, så en ny bruger bliver logget ind og sendt til forsiden.

## Hvad vi byggede

En `RegisterForm`, en `users`-tabel og en `/register`-rute, der gemmer en hashet og saltet adgangskode. `login_user()` kaldes lige efter, at brugeren er gemt.

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

## Sådan ser det ud

![Registreringsformularen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-01-register-form.png)

## Hvad vi fik ud af det

- En formularklasse beskriver felter og validering ét sted; `render_form()` tegner den.
- Gem aldrig en adgangskode: gem den saltede hash.
- At logge brugeren ind lige efter registrering sparer en ekstra formular.

Næste trin: [Log brugere ind](Step-2-Log-In-Users-da) · [Tilbage til oversigten](Home-da)
