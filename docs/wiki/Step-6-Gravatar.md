**English** · [Dansk](Step-6-Gravatar-da) · [Bahasa Malaysia](Step-6-Gravatar-ms)

# Step 6: Add Gravatar profile pictures

## What the lecture asked

Show a profile picture next to every comment. The `flask-gravatar` package is no longer maintained, so build the Gravatar URL yourself from a hash of the email address.

## What we built

A small helper that lowercases and hashes the email and returns the avatar URL. `post.html` shows it next to each comment.

```python
class GravatarAvatarProvider:
    def avatar_url(self, email: str) -> str:
        digest = hashlib.sha256(normalise_email(email).encode()).hexdigest()
        query = urlencode({"s": GRAVATAR_SIZE, "d": GRAVATAR_DEFAULT_IMAGE, "r": GRAVATAR_RATING})
        return f"{GRAVATAR_BASE_URL}/{digest}?{query}"
```

## What it looks like

![Gravatar avatars](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-06-gravatar-avatars.png)

## What we gained

- Gravatar needs only a hash of the email, no account on our side.
- A package that is not maintained can be replaced by a few lines.
- A default image (`d=retro`) covers people without a Gravatar.

Previous step: [Comments](Step-5-Comments) · [Back to the overview](Home)
