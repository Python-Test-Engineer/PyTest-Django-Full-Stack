# Django Local Library

Tutorial "Local Library" website written in Django.

For detailed information about this project see the associated [MDN tutorial home page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).

Repo: [https://github.com/mdn/django-locallibrary-tutorial](https://github.com/mdn/django-locallibrary-tutorial)

## Overview

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

* There are models for books, book copies, genre, language and authors.
* Users can view list and detail information for books and authors.
* Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
* Librarians can renew reserved books.

![Local Library Model](https://raw.githubusercontent.com/mdn/django-locallibrary-tutorial/master/catalog/static/images/local_library_model_uml.png)

## Quick Start

To get this project up and running locally on your computer:
- Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   We recommend using a Python virtual environment.
   > **Note:** This has been tested against Django 3.10 (and may not work or be "optimal" for other versions).
- Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
- Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
- Create a few test objects of each type.
- Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
- login is `admin` and password is `password@2024`.
  
## Styling

Bootstrap CDN is used for styling and was included by MDN.

`catalog\static\css\styles.css` has custom styling.

## Additions

- `pip install rich pyboxen` for console formatting.
- `pip install django-extensions` and add `scripts` folder in project root.


Example use: 
```
# scripts/delete_all_books.py

from catalog.models import Book

def run():
    # Fetch all books
    books = Book.objects.all()
    # Delete books
    questions.delete()
```

`python manage.py runscript delete_all_books`
