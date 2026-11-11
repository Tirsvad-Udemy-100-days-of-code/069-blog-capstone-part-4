[English](Step-3-Protect-Routes) · **Dansk** · [Bahasa Malaysia](Step-3-Protect-Routes-ms)

# Trin 3: Beskyt ruter

## Hvad lektionen bad om

Den første registrerede bruger (id 1) er administrator og den eneste, der må oprette, redigere og slette indlæg. Skjul knapperne for alle andre, og beskyt derefter ruterne med din egen `@admin_only`-dekoratør, der giver en 403-fejl.

## Hvad vi byggede

En `admin_only`-dekoratør bygget som `@login_required` med `functools.wraps`. Skabelonerne får et `is_admin`-flag beregnet ud fra domæneregelen (bruger-id 1), så knapperne er skjult, men kun dekoratøren beskytter ruterne.

```python
def admin_only[**Params, Result](view: Callable[Params, Result]) -> Callable[Params, Result]:
    @wraps(view)
    def guarded(*args: Params.args, **kwargs: Params.kwargs) -> Result:
        if not current_user_is_admin():
            abort(403)
        return view(*args, **kwargs)

    return guarded

# domain/user.py: user id 1 is the admin (ADMIN_USER_ID in constants.py)
```

## Sådan ser det ud

![Administratorvisning: Create New Post, Edit og Delete](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-home.png)

![Medlemsvisning: ingen administratorknapper](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-member-home.png)

![403 til et medlem på /new-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03c-403-forbidden.png)

## Hvad vi fik ud af det

- At skjule en knap er kosmetik; ruten skal beskyttes på serveren.
- En dekoratør omslutter en view-funktion og afgør, om den må køre.
- `abort(403)` er den hurtige måde at svare "ingen adgang" på.

Forrige trin: [Log brugere ind](Step-2-Log-In-Users-da) · Næste trin: [Relationel database](Step-4-Relational-Database-da) · [Tilbage til oversigten](Home-da)
