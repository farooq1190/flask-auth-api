# Flask Authentication API (JWT)

A backend-focused Flask REST API that implements **user registration, login, and JWT-based authentication** using SQLite.  
This project is designed for **learning and demonstrating core backend concepts** with clean architecture and industry-standard practices.

---

## 🚀 Features

- User Registration API
- User Login API
- Secure password hashing
- JWT-based authentication (stateless)
- Protected routes using JWT
- SQLite database integration
- Clean project structure
- Environment-based configuration
- Postman-tested APIs

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **SQLite**
- **JWT (JSON Web Tokens)**
- **Werkzeug Security**
- **python-dotenv**

---

##Project Structure

flask-auth-api/
│
├── app.py # Application entry point
├── auth.py # Authentication routes (register, login, profile)
├── models.py # Database access layer
├── utils.py # JWT utilities
├── config.py # App configuration
├── requirements.txt # Project dependencies
├── .env # Environment variables (ignored in Git)
├── .gitignore
└── venv/ # Virtual environment (ignored in Git)

---
## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/farooq1190/flask-auth-api.git
cd flask-auth-api

### 2️⃣ Create & Activate Virtual Environment
'''bash

python -m venv venv

#### Windows

venv\Scripts\activate

#### Mac/Linux

source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Environment Variables
#### Create a .env file

SECRET_KEY=supersecretkey
 ⚠️ .env is ignored by Git for security.

### 5️⃣ Run the Application

http://127.0.0.1:5000


🧪 API Endpoints

🔹 Register User
Json
{
  "username": "anwar",
  "password": "1234"
}

#### Response
Json

{
  "message": "user created successfully"
}


🔹 Login User
Json
{
  "username": "anwar",
  "password": "1234"
}

#### Response
Json
{
  "token": "JWT_TOKEN"
}

🔹 Protected Profile API

Authorization: Bearer JWT_TOKEN

#### Response
Json
{
  "username": "anwar"
}

🔐 Authentication Flow

-User registers via /api/register

-User logs in via /api/login

-Server returns a JWT token

-Client sends token in Authorization header

-Protected routes verify token before responding

🧠 Key Backend Concepts Covered

-RESTful API design

-Stateless authentication

-JWT creation & verification

-Password hashing & security

-SQLite database handling

-Error handling & HTTP status codes

-Git & GitHub best practices

📌 Notes

-This project is backend-focused (no frontend).

-SQLite is used for simplicity; can be upgraded to PostgreSQL.

-Test routes were used during development and removed before production.

📈 Future Improvements

👉Refresh tokens

👉Role-based access control (RBAC)

👉PostgreSQL integration

👉API documentation with Swagger

👉Dockerization

👉Unit testing


👤 Author

Mohammad farooq
Backend Developer (Learning & Practice Project)





