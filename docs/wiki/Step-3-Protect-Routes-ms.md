[English](Step-3-Protect-Routes) · [Dansk](Step-3-Protect-Routes-da) · **Bahasa Malaysia**

# Langkah 3: Lindungi laluan

## Apa yang diminta dalam kuliah

Pengguna berdaftar pertama (id 1) ialah pentadbir dan satu-satunya yang boleh mencipta, mengedit dan memadam catatan. Sembunyikan butang daripada orang lain, kemudian lindungi laluan dengan dekorator `@admin_only` anda sendiri yang memberi ralat 403.

## Apa yang kami bina

Dekorator `admin_only` yang dibina seperti `@login_required` dengan `functools.wraps`. Templat juga menguji `current_user.id == 1`, jadi butang disembunyikan, tetapi hanya dekorator yang melindungi laluan.

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

## Rupanya

![Lindungi laluan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-only-buttons.png)

![Lindungi laluan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-403-forbidden.png)

Imej ini ialah ilustrasi dengan data contoh, dilukis untuk repositori ini; ia bukan tangkapan skrin projek kursus.

## Apa yang kami perolehi

- Menyembunyikan butang hanyalah hiasan; laluan mesti dilindungi di pelayan.
- Dekorator membungkus fungsi paparan dan menentukan sama ada ia boleh berjalan.
- `abort(403)` ialah cara pantas untuk menjawab "tidak dibenarkan".

Langkah sebelumnya: [Log masuk pengguna](Step-2-Log-In-Users-ms) · Langkah seterusnya: [Pangkalan data hubungan](Step-4-Relational-Database-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
