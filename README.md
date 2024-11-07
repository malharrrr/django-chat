# Django ChatApp

### Real-Time Chat Application with Django Channels

#### Prerequisites
- Make sure you have Python installed (version 3.9 or above is recommended).
- Clone this repository.

### Setup Instructions

1. **Clone this repository:**
   git clone https://github.com/malharrrr/django-chat.git
   cd django-chatapp

2. **Create a virtual environment:**
    python -m venv venv
    source venv/bin/activate  #for macOS
    venv\Scripts\activate.bat  # Windows

3. **Install dependencies:**
    pip/pip3 install -r requirements.txt

4. **Apply database migrations:**
    python/python3 manage.py makemigrations
    python/python3 manage.py migrate

5. **Create a superuser for access to admin panel (localhost:8000/admin || 127.0.0.1/admin):**

    python/python3 manage.py createsuperuser

6. **Start the development server:**
    
    python/python3 manage.py runserver