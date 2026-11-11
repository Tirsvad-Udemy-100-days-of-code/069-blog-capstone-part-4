**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Blog Capstone Part 4: Day 69, users and comments

This wiki explains what each lecture step of Day 69 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" taught us. The lecture finishes the blog: users can register and log in, only the admin manages posts, posts and comments are linked to their authors, logged-in users comment, and every commenter gets a Gravatar picture. The images are illustrations with example data, drawn for this repository.

## Run it

This repository holds documentation only. To follow along, create a local `.venv`, upgrade pip and install the packages that come with the course download (the full instructions are in the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## The six steps

1. [Step 1: Register new users](Step-1-Register-New-Users)
2. [Step 2: Log in registered users](Step-2-Log-In-Users)
3. [Step 3: Protect routes](Step-3-Protect-Routes)
4. [Step 4: Create a relational database](Step-4-Relational-Database)
5. [Step 5: Allow any user to add comments](Step-5-Comments)
6. [Step 6: Add Gravatar profile pictures](Step-6-Gravatar)

## What we gained overall

- Registering and logging in users with Flask-WTF, Werkzeug and Flask-Login.
- Protecting routes with a custom decorator and a 403 error.
- Relational data: one-to-many relationships between users, posts and comments.
- Comments with CKEditor, and Gravatar pictures built from a hash.
