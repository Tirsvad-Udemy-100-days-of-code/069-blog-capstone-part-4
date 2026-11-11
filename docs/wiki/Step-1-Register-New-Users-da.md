[English](Step-1-Register-New-Users) · **Dansk** · [Bahasa Malaysia](Step-1-Register-New-Users-ms)

# Trin 1: Registrer nye brugere

## Hvad lektionen bad om

Lad folk tilmelde sig på `/register`. Lav en `RegisterForm`, en `User`-tabel, hash og salt adgangskoden med Werkzeug, og vis formularen med Bootstrap-Flask. Vent med Flask-Login, og tilføj så én linje, så en ny bruger bliver logget ind og sendt til forsiden.

## Hvad vi byggede

En `RegisterForm`, en `users`-tabel og en `/register`-rute, der gemmer en hashet og saltet adgangskode. `login_user()` kaldes lige efter, at brugeren er gemt.

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

## Sådan ser det ud

![Registrer nye brugere](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-01-register-form.png)

Billedet er en illustration med eksempeldata, tegnet til dette repository; det er ikke et screenshot af kursets projekt.

## Hvad vi fik ud af det

- En formularklasse beskriver felter og validering ét sted; `render_form()` tegner den.
- Gem aldrig en adgangskode: gem den saltede hash.
- At logge brugeren ind lige efter registrering sparer en ekstra formular.

Næste trin: [Log brugere ind](Step-2-Log-In-Users-da) · [Tilbage til oversigten](Home-da)
