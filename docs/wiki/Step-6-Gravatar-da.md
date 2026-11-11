[English](Step-6-Gravatar) · **Dansk** · [Bahasa Malaysia](Step-6-Gravatar-ms)

# Trin 6: Tilføj Gravatar-profilbilleder

## Hvad lektionen bad om

Vis et profilbillede ved hver kommentar. Pakken `flask-gravatar` vedligeholdes ikke længere, så byg selv Gravatar-adressen ud fra en hash af e-mailadressen.

## Hvad vi byggede

En lille hjælper, der gør e-mailen til små bogstaver, hasher den og returnerer billedadressen. `post.html` viser billedet ved hver kommentar.

```python
class GravatarAvatarProvider:
    def avatar_url(self, email: str) -> str:
        digest = hashlib.sha256(normalise_email(email).encode()).hexdigest()
        query = urlencode({"s": GRAVATAR_SIZE, "d": GRAVATAR_DEFAULT_IMAGE, "r": GRAVATAR_RATING})
        return f"{GRAVATAR_BASE_URL}/{digest}?{query}"
```

## Sådan ser det ud

![Gravatar-avatarer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-06-gravatar-avatars.png)

## Hvad vi fik ud af det

- Gravatar kræver kun en hash af e-mailen, ingen konto hos os.
- En pakke, der ikke vedligeholdes, kan erstattes af få linjer.
- Et standardbillede (`d=retro`) dækker dem uden Gravatar.

Forrige trin: [Kommentarer](Step-5-Comments-da) · [Tilbage til oversigten](Home-da)
