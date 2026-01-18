# Library Management System

This project implements a library management system with functionality for books, users, borrowings, and payments. The project is built using **Django + Django REST Framework**, with **JWT authentication** and runs using **Docker**.

---

## 🚀 Core Features

### Books Service
- Full CRUD functionality for books
- Fields: `title`, `author`, `cover` (HARD/SOFT), `inventory`, `daily_fee`
- Access rules:
  - **Admin**: create/update/delete books
  - **All users (including unauthenticated)**: list and view books

### Payments Service
- Payment creation for borrowings
- Fields: `status` (PENDING/PAID), `type` (PAYMENT/FINE), `money_to_pay`, `session_url`, `session_id`, `borrowing`
- List and detail endpoints
- Non-admin users can see only their own payments, admins can see all payments

---

## 🛠 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- djangorestframework-simplejwt (JWT)

## How to start
- git clone https://github.com/Ryu-Tora/drf-library.git
- make .env
- run: docker-compose up --build
