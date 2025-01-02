# Django Authentication Project

A Django web app for user authentication with login, signup, forgot password, change password, dashboard, and profile pages.

---

## Features

- **User Authentication**: Login, signup, forgot password, and change password.
- **Protected Pages**: Dashboard and profile pages for authenticated users.
- **Error Handling**: Clear messages for invalid inputs, email issues, etc.
- **UI Enhancements**: Bootstrap design with auto-closing alerts.

---

## Setup

### Prerequisites
- Python 3.x
- Django 4.x

### Installation

1. **Clone the Repository**
2. **Set Up Virtual Environment :**
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate # On Windows
```
3. **Install Dependencies :**
```bash
pip install -r requirements.txt
```
4. **Run Migrations :**
```bash
python manage.py migrate
```
5. **Run the Server :**
```bash
python manage.py runserver
```
6. **Access the App :**
- Open http://127.0.0.1:8000/auth/login/ in your browser.


---

## Project Structure


```bash
project/
├── userauth/
│   ├── templates/auth/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── forgot_password.html
│   │   └── ...
│   ├── views.py
│   ├── urls.py
│   └── ...
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Notes

1. **Email Setup :**
- For testing, emails are printed to the console. Update settings.py for production:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'email@example.com'
EMAIL_HOST_PASSWORD = 'password'
```
