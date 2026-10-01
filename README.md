# Django Blog

A simple blog website built using Django. This project was created to learn the fundamentals of Django, including URL routing, views, templates, static files, and project structure.

## Features

* Django-based web application
* Home page
* HTML templates using Django Template Language (DTL)
* Custom CSS styling
* Static image and CSS file handling
* SQLite database
* Django development server

## Tech Stack

* Python
* Django
* HTML
* CSS
* SQLite
* Git & GitHub

## Project Structure

```text
blog_main/
├── manage.py
├── blog_main/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── blog.css
│   └── images/
│       └── cricket.jpg
└── templates/
    └── home.html
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd django-blog
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Django

```bash
python -m pip install django
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the development server in your browser at:

```text
http://127.0.0.1:8000/
```

## Static Files

Static files are stored in the `static` directory.

```text
static/
├── css/
│   └── blog.css
└── images/
    └── cricket.jpg
```

Django's static file handling is configured using `STATIC_URL`, `STATICFILES_DIRS`, and `STATIC_ROOT`.

## Learning Goals

This project helped me understand:

* Django project setup
* URL configuration
* Django views
* Templates and DTL
* Static files
* Basic database configuration
* Virtual environments
* Git and GitHub workflow

## Author

**Ranjit Kumar A**

Computer Science Engineering Student

GitHub: https://github.com/ranjitachari5
