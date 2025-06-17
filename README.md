# 🌐 Forex Broker Account Registration Flow

This is a secure user registration system designed for a Forex Broker platform, built with **Django** and **Django Rest Framework (DRF)**. It includes features like email verification, KYC document upload, and token-based authentication — tailored for the Webminix interview assessment.

---

## 🔑 Features

- ✅ User registration via API
- 📧 Email verification with signed token
- 🔐 Token-based login
- 📂 KYC document upload (requires authentication)
- 🔎 Admin can review uploaded KYC files

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django Rest Framework
- Token Authentication
- Gmail SMTP (via App Password)
- Python Decouple (`.env` management)

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/forex-broker-registration.git
cd forex-broker-registration
```

### 2. Create a `.env` file in the root
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

> 🔒 Do **not** use your Gmail password. Use an **App Password** from: https://myaccount.google.com/apppasswords

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

---

## 📡 API Endpoints

| Method | Endpoint            | Description                  | Auth Required |
|--------|---------------------|------------------------------|---------------|
| POST   | `/api/register/`    | Register a new user          | ❌            |
| GET    | `/api/verify-email/`| Verify email from token link | ❌            |
| POST   | `/api/login/`       | Get auth token               | ❌            |
| POST   | `/api/upload-kyc/`  | Upload KYC document          | ✅            |

---

## 🧪 Sample API Usage

### ✅ Register
```http
POST /api/register/
Content-Type: application/json
{
  "username": "john",
  "email": "john@mail.com",
  "password": "SecurePass123"
}
```

### 📩 Verify Email
Click the verification link sent to your email (Gmail SMTP).

### 🔐 Login
```http
POST /api/login/
{
  "username": "john",
  "password": "SecurePass123"
}
```
Response:
```json
{ "token": "your_token_here" }
```

### 📤 Upload KYC
```http
POST /api/upload-kyc/
Authorization: Token your_token_here
Form-data: kyc_document = (upload a file)
```

---

## 📎 Admin Access

- Create a superuser to view users and KYC files:
```bash
python manage.py createsuperuser
```

- Login at `/admin/`

<!-- ---

## 🎥 Optional: Demo Video

[👉 Click here to watch the demo (Loom/YouTube)](https://your-demo-link.com) -->

---

## 📂 License

This project is developed as part of the Webminix interview assessment.