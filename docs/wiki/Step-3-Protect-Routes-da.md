[English](Step-3-Protect-Routes) · **Dansk** · [Bahasa Malaysia](Step-3-Protect-Routes-ms)

# Trin 3: Beskyt ruter

## Hvad lektionen bad om

Den første registrerede bruger (id 1) er administrator og den eneste, der må oprette, redigere og slette indlæg. Skjul knapperne for alle andre, og beskyt derefter ruterne med din egen `@admin_only`-dekoratør, der giver en 403-fejl.

## Hvad vi byggede

En `admin_only`-dekoratør bygget som `@login_required` med `functools.wraps`. Skabelonerne tester også `current_user.id == 1`, så knapperne er skjult, men kun dekoratøren beskytter ruterne.

```python
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    ...
```

## Sådan ser det ud

![Beskyt ruter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-only-buttons.png)

![Beskyt ruter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-403-forbidden.png)

Billedet er en illustration med eksempeldata, tegnet til dette repository; det er ikke et screenshot af kursets projekt.

## Hvad vi fik ud af det

- At skjule en knap er kosmetik; ruten skal beskyttes på serveren.
- En dekoratør omslutter en view-funktion og afgør, om den må køre.
- `abort(403)` er den hurtige måde at svare "ingen adgang" på.

Forrige trin: [Log brugere ind](Step-2-Log-In-Users-da) · Næste trin: [Relationel database](Step-4-Relational-Database-da) · [Tilbage til oversigten](Home-da)
