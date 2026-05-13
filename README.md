# Coderr - Freelance Marketplace API

**Coderr** is a service-based marketplace platform (similar to Fiverr) that connects freelance professionals (Business Users) with clients (Customers). The backend provides a robust API for managing multi-tier service offers, complex order workflows, and a dual-user profile system.

---

## 🚀 Tech Stack

* **Python 3.x**
* **Django 5.x**
* **Django REST Framework (DRF)**
* **Django Filters** (Advanced search & filtering)
* **Token Authentication** (DRF Authtoken)
* **SQLite** (Development) / **PostgreSQL** (Production ready)

---

## ✨ Features

*   **Dual Profile System:** Separate logic and dashboards for `Business` and `Customer` accounts.
*   **Three-Tier Offers:** Support for "Basic", "Standard", and "Premium" service packages within a single offer.
*   **Smart Order Workflow:** Snapshots offer data (price, delivery time) at the moment of purchase to protect transaction integrity.
*   **Review System:** Anti-spam measures (one review per business) and role-based restrictions.
*   **Advanced Filtering:** Search offers by price range, delivery time, or creator.
*   **Global Statistics:** Public endpoint for platform KPIs (total reviews, average rating, active businesses).

---

## 📂 Project Structure

```bash
coderr/
│── auth_app/          # Registration and Login logic
│── profile_app/       # Business & Customer profile management
│── offers_app/        # Multi-tier service offers & details
│── orders_app/        # Order processing and status tracking
│── reviews_app/       # Peer review system and ratings
│── core/              # Project settings & URL routing
│── manage.py
│── requirements.txt
│── README.md
```
## 🛠️ Installation & Setup
1. Clone the repository
```bash
git clone <your-repository-link>
cd coderr
```
2. Setup Virtual Environment
```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Database Migrations
```bash
python manage.py migrate
```
5. Start Development Server
```bash
python manage.py runserver
```
## 📡 API Endpoints

```bash
🔑 Authentication & Profiles
Method,Endpoint,Description
POST,/api/registration/,Create a new account (Business or Customer)
POST,/api/login/,Authenticate user and obtain Auth Token
GET,/api/profiles/business/,List all registered service providers
GET,/api/profiles/customer/,List all registered clients
GET,/api/profiles/{id}/,Retrieve a detailed profile view
```

```bash
💼 Service Offers
Method,Endpoint,Description
GET,/api/offers/,List all offers with advanced search & filters
POST,/api/offers/,Create a new 3-tier offer (Business users only)
GET,/api/offers/{id}/,Retrieve full offer details including all packages
```

```bash
📦 Orders & Reviews
Method,Endpoint,Description
GET,/api/orders/,List all orders related to the authenticated user
PATCH,/api/orders/{id}/,Update order status (Business owner only)
POST,/api/reviews/,"Leave feedback (Customer only, max 1/business)"
GET,/api/base-info/,"Get platform statistics (Total offers, avg rating)"
```

## 📝 Developer Notes

    Permissions: Most write actions require IsAuthenticated. Specific actions check for IsBusinessUser or IsReviewOwner.

    Data Integrity: Orders use a "snapshot" method in the Serializer to ensure that if a Business changes an Offer price later, existing Orders remain unchanged.

    API Documentation: All ViewSets and Serializers include detailed English Docstrings for clear maintenance.

## 📄 License

MIT License - Created for educational purposes.
