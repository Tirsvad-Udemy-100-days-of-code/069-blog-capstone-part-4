**English** · [Dansk](Step-3-Protect-Routes-da) · [Bahasa Malaysia](Step-3-Protect-Routes-ms)

# Step 3: Protect routes

## What the lecture asked

The first registered user (id 1) is the admin and the only one who may create, edit and delete posts. Hide the buttons from everyone else, then protect the routes with your own `@admin_only` decorator that returns a 403 error.

## What we built

An `admin_only` decorator built like `@login_required` with `functools.wraps`. Templates get an `is_admin` flag computed from the domain rule (user id 1), so the buttons are hidden, but only the decorator protects the routes.

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

## What it looks like

![Admin view: Create New Post, Edit and Delete](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-home.png)

![Member view: no admin controls](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-member-home.png)

![403 for a member on /new-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03c-403-forbidden.png)

## What we gained

- Hiding a button is cosmetic; the route must be protected on the server.
- A decorator wraps a view and decides whether it may run.
- `abort(403)` is the quick way to answer "not authorised".

Previous step: [Log in registered users](Step-2-Log-In-Users) · Next step: [Relational database](Step-4-Relational-Database) · [Back to the overview](Home)
