**English** · [Dansk](Step-6-Gravatar-da) · [Bahasa Malaysia](Step-6-Gravatar-ms)

# Step 6: Add Gravatar profile pictures

## What the lecture asked

Show a profile picture next to every comment. The `flask-gravatar` package is no longer maintained, so build the Gravatar URL yourself from a hash of the email address.

## What we built

A small helper that lowercases and hashes the email and returns the avatar URL. `post.html` shows it next to each comment.

```python
def gravatar_url(email, size=100):
    digest = hashlib.sha256(email.strip().lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d=retro&r=g"
```

## What it looks like

![Add Gravatar profile pictures](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-06-gravatar.png)

The image is an illustration with example data, drawn for this repository; it is not a capture of the course project.

## What we gained

- Gravatar needs only a hash of the email, no account on our side.
- A package that is not maintained can be replaced by a few lines.
- A default image (`d=retro`) covers people without a Gravatar.

Previous step: [Comments](Step-5-Comments) · [Back to the overview](Home)
