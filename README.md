# Library Management System

Цей проєкт реалізує систему управління бібліотекою з функціоналом для книг, користувачів, позик та платежів. Проєкт побудований на **Django + Django REST Framework**, з аутентифікацією через **JWT** та запуском через **Docker**.

---

## 🚀 Основні можливості

### Books Service
- CRUD для книг
- Поля: `title`, `author`, `cover` (HARD/SOFT), `inventory`, `daily_fee`
- Доступ:
  - **Admin**: створення/редагування/видалення книг
  - **Усі користувачі (навіть неавторизовані)**: перегляд списку книг

### Payments Service
- Створення платежів за позики
- Поля: `status` (PENDING/PAID), `type` (PAYMENT/FINE), `money_to_pay`, `session_url`, `session_id`, `borrowing`
- List та Detail endpoints
- Non-admin бачить лише свої платежі, admin — всі

---

## 🛠 Стек технологій

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- djangorestframework-simplejwt (JWT)

## How to start
- git clone https://github.com/Ryu-Tora/drf-library.git
- make .env
- run: docker-compose up --build
