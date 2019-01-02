# Django CRUD

Documentation for a Django CRUD site. The site is meant to display CRUD features end to end from being able to create a entry of daily item expense. The form accepts the basic item attributes such as title, type, amount, location, image, and comments. The app was initially named 'the grocer' because it was to help record grocery expenses. It does so with a basic create form, while the index page lists the entries. Edit and delete features are available upon accessing an entry's detail page. The site uses basic HTML with little to no CSS as this project was just intended to display CRUD and not include any styling at the moment. Future projects will use CSS for positioning and organization purposes.

---

Project source can be downloaded from https://github.com/iaingoh/django-crud.git

---

## Author & Contributor List

Iain Goh

---

## File List

```
.:
db.sqlite3
manage.py
README.md
./expenses
./media
./the_grocer
```
```
/the_grocer:
__init__.py
settings.py
urls.py
wsgi.py
```
```
/expenses:
./migrations
./templates
__init__.py
admin.py
apps.py
forms.py
models.py
tests.py
urls.py
views.py
```
```
/media:
./uploads
```

## How to run file
Django should already be installed to run this project. If not, you may do so via either pipenv or pip via the following commands:
```
pipenv install django
```

Find the project parent directory, and locate manage.py .
Run python manage.py runserver

With the localhost address, paste it into the browser's address bar and from there you will be redirected to the project's home page.

---

## Project's URL routes run on the development server

```
http://localhost/admin/
http://localhost/expenses/
http://localhost/expenses/index/
http://localhost/expenses/new/
http://localhost/expenses/success/
http://localhost/expenses/detail/<pk>
http://localhost/expenses/update/<pk>
http://localhost/expenses/delete/<pk>
```
*Where pk is the item's primary key

---

## To do
- Add favicon