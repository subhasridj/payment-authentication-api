 Payment Authentication API

A secure backend system for handling user authentication and payment-related operations using FastAPI and JWT.

---
Features

* User registration & login
* JWT-based authentication
* Secure password hashing
* Modular API design
* Database integration (SQLite)

---
 Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* JWT (JSON Web Tokens)

---
Project Structure

```
.
├── api/
│   ├── main.py
│   ├── routes/
│   │   └── auth.py
│   ├── core/
│   │   └── security.py
├── database.py
├── models.py
├── crud.py
├── requirements.txt
```

---

 Installation & Run

```bash
git clone https://github.com/your-username/payment-authentication-api.git
cd payment-authentication-api

pip install -r requirements.txt
uvicorn api.main:app --reload
```

---

## 🔐 Authentication Flow

1. User registers with email & password
2. Password is hashed and stored securely
3. User logs in → JWT token generated
4. Token used for accessing protected routes

API Endpoints

* `POST /register` → Create user
* `POST /login` → Authenticate user
* `GET /profile` → Protected route

 🎯 Use Case

* Fintech applications
* Secure login systems
* Payment gateway backends

Future Improvements

* Add payment gateway integration (Stripe/Razorpay)
* Role-based access control
* Deploy using Docker & AWS

---
