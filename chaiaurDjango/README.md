# ChaiAurDjango API Documentation

This Django project now includes REST API endpoints with automatic API documentation.

## Setup

1. Activate the virtual environment:
   ```
   & "c:\Users\monal\OneDrive\Desktop\Python\probably Django\.venv\Scripts\Activate.ps1"
   ```

2. Run migrations:
   ```
   python manage.py migrate
   ```

3. Start the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Chai Varieties
- **GET/POST/PUT/DELETE** `/chai/api/chai-varieties/`
- **GET/POST/PUT/DELETE** `/chai/api/chai-varieties/{id}/`

### Available Teas
- **GET/POST/PUT/DELETE** `/chai/api/available-teas/`
- **GET/POST/PUT/DELETE** `/chai/api/available-teas/{id}/`

## API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/redoc/`

## Models

### ChaiVarity
- name: CharField
- image: ImageField
- date_added: DateTimeField
- type: CharField (choices)
- description: TextField
- price: DecimalField

### AvailableTea
- name: CharField
- image: ImageField
- date_added: DateTimeField
- type: CharField (choices)
- description: TextField
- price: DecimalField

## Technologies Used

- Django 6.0
- Django REST Framework
- drf-yasg (for OpenAPI/Swagger documentation)
- SQLite database