**English** · [Dansk](Step-3-Protect-Routes-da) · [Bahasa Malaysia](Step-3-Protect-Routes-ms)

# Step 3: Protect routes

## What the lecture asked

The first registered user (id 1) is the admin and the only one who may create, edit and delete posts. Hide the buttons from everyone else, then protect the routes with your own `@admin_only` decorator that returns a 403 error.

## What we built

An `admin_only` decorator built like `@login_required` with `functools.wraps`. Templates also test `current_user.id == 1`, so the buttons are hidden, but only the decorator protects the routes.

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

## What it looks like

![Protect routes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-only-buttons.png)

![Protect routes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-403-forbidden.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- Hiding a button is cosmetic; the route must be protected on the server.
- A decorator wraps a view and decides whether it may run.
- `abort(403)` is the quick way to answer "not authorised".

Previous step: [Log in registered users](Step-2-Log-In-Users) · Next step: [Relational database](Step-4-Relational-Database) · [Back to the overview](Home)
