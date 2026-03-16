# ☕ Chai Ki Dukan

**Chai Ki Dukan** is a Django-based web application for browsing and ordering different varieties of tea.
The project demonstrates a complete web workflow including user authentication, product browsing, and cart management.

---

## 🚀 Features

* 🔐 User Authentication (Login / Signup)
* 🛍️ Browse available tea varieties
* ➕ Add items to cart
* 🛒 Cart management system
* 🎨 Clean and modern UI
* 📱 Responsive layout

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
chai-ki-dukan/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── chai/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── chaiapp/              # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/            # HTML templates
└── static/               # CSS, JS, images
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/MonaLisa-20-04/chai-ki-dukan.git
```

Move into the project folder:

```
cd chai-ki-dukan
```

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate the virtual environment:

**Windows**

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Start the development server:

```
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

---

## 🎯 Learning Goals

This project helped me practice:

* Django project structure
* Django models and migrations
* User authentication system
* Cart logic implementation
* Frontend and backend integration

---

## 🔮 Future Improvements

* 💳 Payment gateway integration
* ⭐ Product reviews and ratings
* 📦 Order history
* 🔍 Search and filtering

---

## 👨‍💻 Author

Developed by a Computer Engineering student exploring **full-stack web development with Django**.

---
