# 🛒 Django DRF Ecommerce

An Ecommerce REST API built with Django and Django REST Framework for managing products, categories, and more.

[👉 **View the Demo**](https://ecommerce-bold-bird-4463.fly.dev/api/schema/docs/)

---

## 🚀 Features

- Product and Category Management
- RESTful API Endpoints using Django REST Framework
- SQLite (local) / PostgreSQL (production) support
- Dockerized for easy deployment (e.g., Fly.io)
- Environment-based settings (`local.py`, `production.py`)
- Token-based authentication (optional)
- Admin dashboard for managing data

---

## 🧰 Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL / SQLite
- Docker
- Fly.io (deployment)

---

## 📦 Installation

### Local Development

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/django-ecommerce.git
   cd django-ecommerce
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set environment variables:**  
   Create a `.env` file or export variables in your shell:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```
5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### Deployment (Fly.io Example)

1. **Deploy to Fly.io:**
   ```bash
   flyctl deploy
   ```
2. **Set secrets:**
   ```bash
   fly secrets set SECRET_KEY=your-secret-key
   fly secrets set DJANGO_SETTINGS_MODULE=ecommerce.settings.production
   fly secrets set DATABASE_URL=your-postgres-url
   fly secrets set ALLOWED_HOSTS=ecommerce-bold-bird-4463.fly.dev
   ```

---

## 📚 API Endpoints

| Method | Endpoint              | Description         |
| ------ | --------------------- | ------------------- |
| GET    | `/api/products/`      | List all products   |
| GET    | `/api/products/<id>/` | Retrieve a product  |
| POST   | `/api/products/`      | Create a product    |
| GET    | `/api/categories/`    | List all categories |
| POST   | `/api/categories/`    | Create a category   |
