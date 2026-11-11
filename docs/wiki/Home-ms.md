[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Blog Capstone Part 4: Hari 69, pengguna dan komen

Wiki ini menerangkan apa yang diajar oleh setiap langkah kuliah hari ke-69 kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp". Kuliah ini melengkapkan blog: pengguna boleh mendaftar dan log masuk, hanya pentadbir menguruskan catatan, catatan dan komen dikaitkan dengan penulisnya, pengguna yang log masuk memberi komen, dan setiap pemberi komen mendapat gambar Gravatar. Tangkapan skrin datang daripada blog repositori ini sendiri, dijalankan dalam bekas Docker dengan data contoh.

## Jalankannya

Repositori ini mengandungi blog yang ditulis untuk kuliah ini. Cipta `.venv` setempat, naik taraf pip, pasang pakej yang dikunci dan mulakan blog (arahan lengkap ada dalam [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
python -m blog
```

## Enam langkah

1. [Langkah 1: Daftarkan pengguna baharu](Step-1-Register-New-Users-ms)
2. [Langkah 2: Log masuk pengguna berdaftar](Step-2-Log-In-Users-ms)
3. [Langkah 3: Lindungi laluan](Step-3-Protect-Routes-ms)
4. [Langkah 4: Cipta pangkalan data hubungan](Step-4-Relational-Database-ms)
5. [Langkah 5: Benarkan mana-mana pengguna menambah komen](Step-5-Comments-ms)
6. [Langkah 6: Tambah gambar profil Gravatar](Step-6-Gravatar-ms)

## Apa yang kami perolehi secara keseluruhan

- Mendaftar dan log masuk pengguna dengan Flask-WTF, Werkzeug dan Flask-Login.
- Melindungi laluan dengan dekorator sendiri dan ralat 403.
- Data berhubung: hubungan satu-ke-banyak antara pengguna, catatan dan komen.
- Komen dengan CKEditor, dan gambar Gravatar yang dibina daripada cincang.
