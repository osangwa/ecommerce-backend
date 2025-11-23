# 🛍️ E-Commerce Backend API

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-13-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> A production-ready e-commerce backend API built with Django REST Framework, focusing on scalability, performance, and clean architecture.

**Live API:** [Coming Soon](#) | **Documentation:** [API Docs](#)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#️-database-schema)
- [API Usage Examples](#-api-usage-examples)
- [Development](#-development)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project is a **robust backend system** for an e-commerce platform, developed as part of the **ProDev Backend Engineering Program**. It demonstrates enterprise-level backend development practices with emphasis on:

- ✅ **RESTful API Design** - Clean, intuitive endpoints
- ✅ **Database Optimization** - Efficient queries and indexing
- ✅ **Security** - JWT authentication and data protection
- ✅ **Performance** - Redis caching and query optimization
- ✅ **Documentation** - Interactive Swagger/OpenAPI docs

### 🎓 Learning Objectives

- Design and optimize relational database schemas
- Build secure and scalable REST APIs
- Implement authentication and authorization
- Apply performance optimization techniques
- Follow industry best practices for backend development

---

## ✨ Features

### Core Functionality

#### 🔐 Authentication & Authorization
- User registration and login with JWT tokens
- Token refresh mechanism
- Password reset functionality
- Role-based access control (User/Admin)

#### 📦 Product Management
- Full CRUD operations for products
- Product image upload and management
- Inventory tracking
- Category-based organization
- Search functionality by name and description

#### 🗂️ Category System
- Hierarchical category structure
- Category-based product filtering
- Easy navigation and organization

#### 🔍 Advanced Features
- **Filtering** - By category, price range, availability
- **Sorting** - By price, name, date added, popularity
- **Pagination** - Efficient handling of large datasets
- **Search** - Full-text search across products

#### 🛒 Shopping Cart (Coming Soon)
- Add/remove items
- Update quantities
- Session-based cart management

#### 📋 Order Management (Coming Soon)
- Order creation and tracking
- Order history
- Status updates

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend Framework** | Django 4.2 + DRF | REST API development |
| **Database** | PostgreSQL 13+ | Primary data storage |
| **Authentication** | JWT (SimpleJWT) | Secure token-based auth |
| **Caching** | Redis 6+ | Performance optimization |
| **API Documentation** | Swagger/OpenAPI | Interactive docs |
| **Testing** | pytest + Django TestCase | Automated testing |
| **Deployment** | Docker + Render | Production hosting |

### Key Libraries
```
Django==4.2
djangorestframework==3.14
djangorestframework-simplejwt==5.3
psycopg2-binary==2.9
django-cors-headers==4.3
drf-yasg==1.21  # Swagger docs
redis==5.0
Pillow==10.1  # Image handling
```

---

## 📁 Project Structure

```
ecommerce-backend/
│
├── config/                 # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── authentication/     # User auth & JWT
│   ├── products/          # Product management
│   ├── categories/        # Category system
│   ├── cart/             # Shopping cart (WIP)
│   └── orders/           # Order processing (WIP)
│
├── static/               # Static files
├── media/                # Uploaded files
├── tests/                # Test suites
├── docker/               # Docker configuration
├── requirements/         # Dependencies
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
│
├── .env.example         # Environment variables template
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python 3.11+**
- **PostgreSQL 13+**
- **Redis 6+** (optional for caching)
- **Git**

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/osangwa/ecommerce-backend.git
cd ecommerce-backend
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements/dev.txt
```

#### 4. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
nano .env  # or use your preferred editor
```

**Sample `.env` file:**
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Redis (optional)
REDIS_URL=redis://localhost:6379/0

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutes
```

#### 5. Database Setup
```bash
# Create database (PostgreSQL)
createdb ecommerce_db

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# (Optional) Load sample data
python manage.py loaddata fixtures/sample_data.json
```

#### 6. Run Development Server
```bash
python manage.py runserver
```

The API will be available at: **http://localhost:8000/**

API Documentation: **http://localhost:8000/api/docs/**

---

## 🐳 Docker Setup (Alternative)

```bash
# Build and start containers
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

Access at: **http://localhost:8000/**

---

## 🔌 API Endpoints

### Authentication
```http
POST   /api/auth/register/              # Register new user
POST   /api/auth/login/                 # Login (get JWT tokens)
POST   /api/auth/token/refresh/         # Refresh access token
POST   /api/auth/logout/                # Logout
GET    /api/auth/profile/               # Get user profile
PUT    /api/auth/profile/               # Update user profile
```

### Products
```http
GET    /api/products/                   # List products (with filters)
POST   /api/products/                   # Create product (Admin only)
GET    /api/products/{id}/              # Product detail
PUT    /api/products/{id}/              # Update product (Admin only)
PATCH  /api/products/{id}/              # Partial update (Admin only)
DELETE /api/products/{id}/              # Delete product (Admin only)
```

#### Query Parameters for Product List
```
?category=electronics          # Filter by category
?min_price=100                # Minimum price
?max_price=1000              # Maximum price
?search=laptop               # Search in name/description
?ordering=-price             # Sort by price (desc)
?ordering=name               # Sort by name (asc)
?page=1                      # Pagination
?page_size=20                # Items per page
```

### Categories
```http
GET    /api/categories/                 # List all categories
POST   /api/categories/                 # Create category (Admin only)
GET    /api/categories/{id}/            # Category detail
PUT    /api/categories/{id}/            # Update category (Admin only)
DELETE /api/categories/{id}/            # Delete category (Admin only)
```

### Cart (Coming Soon)
```http
GET    /api/cart/                       # Get cart contents
POST   /api/cart/items/                 # Add item to cart
PUT    /api/cart/items/{id}/            # Update item quantity
DELETE /api/cart/items/{id}/            # Remove item from cart
DELETE /api/cart/clear/                 # Clear entire cart
```

### Orders (Coming Soon)
```http
GET    /api/orders/                     # List user orders
POST   /api/orders/                     # Create new order
GET    /api/orders/{id}/                # Order detail
PUT    /api/orders/{id}/cancel/         # Cancel order
```

---

## 🗄️ Database Schema

### Core Models

```python
# User (Django built-in + custom fields)
User
├── email (unique)
├── first_name
├── last_name
├── is_active
└── date_joined

# Category
Category
├── name
├── slug (unique)
├── description
├── parent (self-referential)
└── created_at

# Product
Product
├── name
├── slug (unique)
├── description
├── price (decimal)
├── stock_quantity
├── category (FK)
├── is_available
├── created_at
└── updated_at

# ProductImage
ProductImage
├── product (FK)
├── image
├── alt_text
└── is_primary

# Cart (Coming Soon)
Cart
├── user (FK, nullable)
├── session_id
├── created_at
└── updated_at

# CartItem (Coming Soon)
CartItem
├── cart (FK)
├── product (FK)
├── quantity
└── added_at

# Order (Coming Soon)
Order
├── user (FK)
├── status
├── total_amount
├── shipping_address
├── created_at
└── updated_at
```

### Database Indexes

For optimal performance, the following indexes are applied:

```python
# Products
- Index on: category_id
- Index on: price
- Index on: created_at
- Full-text index on: name, description

# Categories
- Index on: slug
- Index on: parent_id

# Orders
- Index on: user_id
- Index on: status
- Index on: created_at
```

---

## 📊 API Usage Examples

### 1. User Registration
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123!",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

**Response:**
```json
{
  "id": 1,
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

### 2. Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123!"
  }'
```

### 3. List Products with Filters
```bash
curl -X GET "http://localhost:8000/api/products/?category=electronics&min_price=500&max_price=2000&ordering=-price&page=1"
```

**Response:**
```json
{
  "count": 45,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "MacBook Pro 16\"",
      "slug": "macbook-pro-16",
      "description": "Powerful laptop for professionals",
      "price": "1999.99",
      "stock_quantity": 15,
      "category": {
        "id": 2,
        "name": "Laptops"
      },
      "images": [
        {
          "image": "/media/products/macbook-pro.jpg",
          "is_primary": true
        }
      ],
      "is_available": true,
      "created_at": "2024-11-20T10:30:00Z"
    }
  ]
}
```

### 4. Create Product (Admin)
```bash
curl -X POST http://localhost:8000/api/products/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse",
    "price": "29.99",
    "stock_quantity": 100,
    "category": 5,
    "is_available": true
  }'
```

### 5. Search Products
```bash
curl -X GET "http://localhost:8000/api/products/?search=wireless+mouse"
```

---

## 👨‍💻 Development

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.products

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Code Quality
```bash
# Format code with black
black .

# Check code style
flake8 .

# Sort imports
isort .
```

### Database Management
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database
python manage.py flush

# Export data
python manage.py dumpdata > backup.json

# Import data
python manage.py loaddata backup.json
```

### Create Sample Data
```bash
# Run custom management command
python manage.py create_sample_data
```

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use strong `SECRET_KEY`
- [ ] Set up PostgreSQL (managed service)
- [ ] Configure Redis for caching
- [ ] Set up static file serving (WhiteNoise/CDN)
- [ ] Configure HTTPS/SSL
- [ ] Set up environment variables
- [ ] Enable CORS for frontend domain
- [ ] Configure database backups
- [ ] Set up monitoring and logging

### Deploy to Render

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: ecommerce-api
    env: python
    buildCommand: pip install -r requirements/prod.txt && python manage.py migrate
    startCommand: gunicorn config.wsgi:application
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: ecommerce-db
          property: connectionString
```

2. Push to GitHub and connect to Render

### Deploy with Docker
```bash
# Build production image
docker build -t ecommerce-api:prod -f docker/Dockerfile.prod .

# Run container
docker run -p 8000:8000 --env-file .env.prod ecommerce-api:prod
```

---

## 📈 Performance Optimization

### Implemented Optimizations

1. **Database Query Optimization**
   - Use of `select_related()` for foreign keys
   - Use of `prefetch_related()` for reverse relations
   - Database indexing on frequently queried fields

2. **Caching Strategy**
   - Redis caching for product listings
   - Cache frequently accessed data
   - Cache invalidation on updates

3. **API Response Optimization**
   - Pagination for large datasets
   - Minimal serializer fields
   - Efficient queryset filtering

4. **Security Measures**
   - JWT token authentication
   - CORS configuration
   - Input validation and sanitization
   - SQL injection prevention via ORM
   - XSS protection

---

## 🎯 Development Roadmap

### Phase 1: Foundation ✅ (Completed)
- [x] Django project setup
- [x] PostgreSQL configuration
- [x] User authentication with JWT
- [x] Product CRUD APIs
- [x] Category system
- [x] Filtering and pagination
- [x] API documentation

### Phase 2: Core Features 🚧 (In Progress)
- [ ] Shopping cart functionality
- [ ] Order management system
- [ ] Product reviews and ratings
- [ ] Wishlist feature
- [ ] Email notifications

### Phase 3: Advanced Features 📋 (Planned)
- [ ] Payment integration (Stripe)
- [ ] Inventory management
- [ ] Admin dashboard APIs
- [ ] Analytics endpoints
- [ ] Search optimization (Elasticsearch)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Commit Message Convention
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Format code
refactor: Refactor code
test: Add tests
perf: Performance improvement
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Octave Sangwa**

- GitHub: [@osangwa](https://github.com/osangwa)
- LinkedIn: [Octave Sangwa](https://linkedin.com/in/osangwa)
- Email: octave.sangwa@example.com

---

## 🙏 Acknowledgments

- ProDev Backend Engineering Program
- Django and DRF communities
- All contributors and supporters

---

## 📞 Support

For questions or issues:
- Open an [issue](https://github.com/osangwa/ecommerce-backend/issues)
- Email: octave.sangwa@example.com

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Octave Sangwa](https://github.com/osangwa)

</div>