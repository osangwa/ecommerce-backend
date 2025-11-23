# 🛍️ E-Commerce Backend API

A production-ready, scalable backend system for a modern e-commerce platform built with Django REST Framework. This project demonstrates enterprise-level backend development with focus on performance, security, and maintainability.

## 🎯 What I am Building

I am creating a complete e-commerce backend system that powers online shopping platforms with:

### 🏗️ Core System Architecture
- **RESTful API** serving web/mobile applications
- **PostgreSQL database** with optimized schema design
- **JWT-based authentication** for secure user management
- **Redis caching** for high-performance data retrieval

### 🚀 Key Business Features
- **Product Catalog** - Complete product management with categories
- **User Authentication** - Secure registration, login, and profile management
- **Shopping Cart** - Session-based cart functionality
- **Order Processing** - Complete order lifecycle management
- **Search & Discovery** - Advanced product filtering and search

### ⚡ Performance & Scalability
- Database indexing for fast queries
- Paginated responses for large datasets
- Caching strategies with Redis
- Optimized API responses with selective field loading

---

## 📋 Project Specifications

### ✅ MVP Features (Must Have)
- ✅ **User Authentication** - JWT-based registration/login
- ✅ **Product Management** - CRUD operations for products
- ✅ **Category System** - Hierarchical product categorization
- ✅ **Advanced Filtering** - Filter by category, price range, ratings
- ✅ **Search Functionality** - Product search by name/description
- ✅ **Shopping Cart** - Add/remove items, quantity management
- ✅ **Order System** - Create, view, and manage orders
- ✅ **API Documentation** - Interactive Swagger/OpenAPI docs

### 🎁 Enhanced Features (Should Have)
- 🔄 **Product Reviews & Ratings** - User feedback system
- 🔄 **Inventory Management** - Stock tracking and updates
- 🔄 **Wishlist** - Save products for later
- 🔄 **Order Status Tracking** - Real-time order updates
- 🔄 **Admin Dashboard** - Administrative controls

### 🚀 Advanced Features (Could Have)
- 💳 **Payment Integration** - Stripe/PayPal payment processing
- 📧 **Email Notifications** - Order confirmations and updates
- 🤖 **Recommendation Engine** - Personalized product suggestions
- 📊 **Analytics Endpoints** - Sales and product analytics
- 🏪 **Multi-vendor Support** - Vendor management system

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Backend Framework | Django 4.2 + Django REST Framework | API development |
| Database | PostgreSQL 13 | Primary data storage |
| Authentication | JWT (Simple JWT) | Secure user auth |
| Caching | Redis | Performance optimization |
| API Docs | Swagger/OpenAPI | Interactive documentation |
| Deployment | Docker + Render/Railway | Production hosting |
| Testing | pytest | Test automation |

---

## 🗄️ Database Schema Overview

### Core Models
```
User → Profile → Address
Category → Product → ProductImage, Review
Cart → CartItem
Order → OrderItem → OrderStatus
```

### Key Relationships
- Users can have multiple **Addresses** and **Orders**
- Products belong to **Categories** (hierarchical)
- Carts contain multiple **CartItems** (session-based)
- Orders consist of multiple **OrderItems**
- Products can have multiple **Reviews** and **Images**

---

## 🔌 API Endpoints Structure

### Authentication & Users
```
POST /api/auth/register/          # User registration
POST /api/auth/login/             # JWT token obtain
POST /api/auth/logout/            # User logout
GET  /api/users/profile/          # User profile management
```

### Products & Catalog
```
GET    /api/products/             # List products (with filtering)
GET    /api/products/{id}/        # Product details
POST   /api/products/             # Create product (Admin)
PUT    /api/products/{id}/        # Update product (Admin)
GET    /api/categories/           # List categories
```

### Shopping Cart
```
GET    /api/cart/                 # Get cart contents
POST   /api/cart/add/             # Add item to cart
PUT    /api/cart/update/{id}/     # Update cart item quantity
DELETE /api/cart/remove/{id}/     # Remove item from cart
```

### Orders
```
GET    /api/orders/               # User's order history
POST   /api/orders/create/        # Create new order
GET    /api/orders/{id}/          # Order details
PUT    /api/orders/{id}/cancel/   # Cancel order
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 13+
- Redis 6+

### Installation

1. **Clone repository**
```bash
git clone https://github.com/osangwa/ecommerce-backend.git
cd ecommerce-backend
```

2. **Setup virtual environment**
```bash
python -m venv ecommerce_env
source ecommerce_env/bin/activate  # On Windows: ecommerce_env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment setup**
```bash
cp .env.example .env
# Configure your database and Redis settings in .env
```

5. **Database setup**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

### Docker Setup

```bash
# Using Docker Compose
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate
```

---

## 📊 API Usage Examples

### Product Filtering
```http
GET /api/products/?category=electronics&min_price=100&max_price=1000&search=laptop&ordering=-price&page=1
```

### Order Creation
```http
POST /api/orders/create/
Content-Type: application/json

{
  "shipping_address": 1,
  "payment_method": "credit_card",
  "items": [
    {"product": 1, "quantity": 2},
    {"product": 3, "quantity": 1}
  ]
}
```

### User Registration
```http
POST /api/auth/register/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123",
  "first_name": "John",
  "last_name": "Doe"
}
```

---

## 🎯 Development Progress

### Current Phase: Foundation Setup ✅
- ✅ Project initialization with Django
- ✅ PostgreSQL database configuration
- ✅ Basic project structure
- ✅ Git repository setup

### Next Phase: Core Features 🚧
- 🔄 User authentication system
- 🔄 Product and category models
- 🔄 Basic CRUD APIs
- 🔄 API documentation setup

---

## 🔒 Security Features

- JWT Authentication with refresh tokens
- Password hashing with Django's built-in security
- CORS configuration for frontend integration
- Input validation and sanitization
- SQL injection prevention with Django ORM
- XSS protection measures

---

## 📈 Performance Optimizations

- Database indexing on frequently queried fields
- Query optimization with `select_related` and `prefetch_related`
- Redis caching for product listings and user sessions
- Paginated responses for large datasets
- Efficient serialization with minimal database hits

---

## 🧪 Testing Strategy

```bash
# Run test suite
python manage.py test

# Test with coverage
coverage run manage.py test
coverage report

# API testing
python manage.py test products.tests.APITestCase
```

---

## 🚀 Deployment

### Production Environment
- **Platform:** Render/Railway
- **Database:** PostgreSQL (managed)
- **Cache:** Redis (managed)
- **Static Files:** WhiteNoise + CDN
- **SSL:** HTTPS enforcement

### Environment Variables
```env
DEBUG=False
SECRET_KEY=your-production-secret
DATABASE_URL=postgresql://user:pass@host:5432/dbname
REDIS_URL=redis://host:6379/0
ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
```

---

## 👥 Project Team

**Developer:** Octave Sangwa

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **Live API:** Coming after deployment
- **API Documentation:** Will be available at `/api/docs/`
- **Frontend Repository:** Separate frontend project

---

## 💡 Project Vision

This isn't just another backend project—it's a production-ready e-commerce solution that demonstrates modern backend development practices. By completion, this will be a portfolio-grade application showcasing scalability, security, and performance optimization techniques used in real-world e-commerce platforms.

**Ready to build something amazing!** 🚀

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/osangwa/ecommerce-backend/issues).

## ⭐ Show your support

Give a ⭐️ if this project helped you!