[English](Step-3-Protect-Routes) · [Dansk](Step-3-Protect-Routes-da) · **Bahasa Malaysia**

# Langkah 3: Lindungi laluan

## Apa yang diminta dalam kuliah

Pengguna berdaftar pertama (id 1) ialah pentadbir dan satu-satunya yang boleh mencipta, mengedit dan memadam catatan. Sembunyikan butang daripada orang lain, kemudian lindungi laluan dengan dekorator `@admin_only` anda sendiri yang memberi ralat 403.

## Apa yang kami bina

Dekorator `admin_only` yang dibina seperti `@login_required` dengan `functools.wraps`. Templat menerima bendera `is_admin` yang dikira daripada peraturan domain (id pengguna 1), jadi butang disembunyikan, tetapi hanya dekorator yang melindungi laluan.

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

## Rupanya

![Paparan pentadbir: Create New Post, Edit dan Delete](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03a-admin-home.png)

![Paparan ahli: tiada kawalan pentadbir](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03b-member-home.png)

![403 untuk ahli pada /new-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/raw/branch/main/docs/images/step-03c-403-forbidden.png)

## Apa yang kami perolehi

- Menyembunyikan butang hanyalah hiasan; laluan mesti dilindungi di pelayan.
- Dekorator membungkus fungsi paparan dan menentukan sama ada ia boleh berjalan.
- `abort(403)` ialah cara pantas untuk menjawab "tidak dibenarkan".

Langkah sebelumnya: [Log masuk pengguna](Step-2-Log-In-Users-ms) · Langkah seterusnya: [Pangkalan data hubungan](Step-4-Relational-Database-ms) · [Kembali ke gambaran keseluruhan](Home-ms)
