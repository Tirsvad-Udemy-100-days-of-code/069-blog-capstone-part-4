[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Blog Capstone Part 4: Dag 69, brugere og kommentarer

Denne wiki forklarer, hvad hvert lektionstrin på dag 69 af Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp" lærte os. Lektionen gør bloggen færdig: brugere kan registrere sig og logge ind, kun administratoren styrer indlæg, indlæg og kommentarer er knyttet til deres forfattere, indloggede brugere kommenterer, og hver kommentator får et Gravatar-billede. Billederne er illustrationer med eksempeldata, tegnet til dette repository.

## Kør det

Dette repository indeholder kun dokumentation. For at følge med skal du oprette en lokal `.venv`, opgradere pip og installere de pakker, der følger med kursets download (hele vejledningen står i [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## De seks trin

1. [Trin 1: Registrer nye brugere](Step-1-Register-New-Users-da)
2. [Trin 2: Log registrerede brugere ind](Step-2-Log-In-Users-da)
3. [Trin 3: Beskyt ruter](Step-3-Protect-Routes-da)
4. [Trin 4: Opret en relationel database](Step-4-Relational-Database-da)
5. [Trin 5: Lad alle brugere skrive kommentarer](Step-5-Comments-da)
6. [Trin 6: Tilføj Gravatar-profilbilleder](Step-6-Gravatar-da)

## Hvad vi fik ud af det samlet set

- At registrere og logge brugere ind med Flask-WTF, Werkzeug og Flask-Login.
- At beskytte ruter med en egen dekoratør og en 403-fejl.
- Relationelle data: en-til-mange-relationer mellem brugere, indlæg og kommentarer.
- Kommentarer med CKEditor og Gravatar-billeder bygget ud fra en hash.
