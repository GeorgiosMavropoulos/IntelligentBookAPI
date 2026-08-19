# 📚 Bookstore API

A small **Bookstore REST API** built with **FastAPI** and **PostgreSQL**.

The goal of this project is to build a realistic backend application while practicing REST APIs, database relationships, authentication, migrations, testing, Docker, and eventually AI agents.

---

## 🚀 Tech Stack

* **FastAPI** — REST API
* **PostgreSQL** — relational database
* **SQLAlchemy 2.0** — ORM
* **Pydantic** — validation & schemas
* **Alembic** — database migrations
* **JWT** — authentication
* **Pytest** — testing
* **Docker / Docker Compose** — development environment

### Extra

* 🤖 AI Agent / Chat
* 📖 Book information & recommendations
* 🔎 Natural-language search
* 🧠 LLM integration

---

## 🎯 Project Goals

The project is divided into multiple phases.

### Phase 1 — Core API

Build a REST API for:

* Users
* Books
* Orders
* Order items

### Phase 2 — Authentication

Add:

* User registration
* Login
* Password hashing
* JWT authentication
* User/admin roles

### Phase 3 — Advanced API

Add:

* Pagination
* Search
* Filtering
* Sorting
* Database transactions
* Validation
* Error handling

### Phase 4 — AI Book Agent 🤖

Add a chat agent that can provide information about books.

Example questions:

> "Do you have any books by Tolkien?"

> "Which books are available for less than €20?"

> "Tell me about Dune."

> "What fantasy books do you recommend?"

> "Which books are currently in stock?"

The agent will eventually be able to interact with the bookstore API/database through tools.

---

## 🏗️ Planned Architecture

```text
                    ┌─────────────────┐
                    │     Client      │
                    │ Web / Postman   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │      REST       │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
        ┌───────────────┐        ┌────────────────┐
        │  PostgreSQL   │        │   AI Agent     │
        │   Database    │        │    (Phase 4)   │
        └───────────────┘        └───────┬────────┘
                                         │
                                         ▼
                                  Book/API Tools
```

The AI agent will **not** be built initially.

The first goal is to create a clean and reliable API that the agent can use later.

---

## 📁 Project Structure

Planned structure:

```text
bookstore-api/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes/
│   │       ├── users.py
│   │       ├── books.py
│   │       └── orders.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── order.py
│   │   └── order_item.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── order.py
│   │   └── auth.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── book_service.py
│   │   └── order_service.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   └── core/
│       ├── config.py
│       └── security.py
│
├── alembic/
│
├── tests/
│   ├── test_users.py
│   ├── test_books.py
│   └── test_orders.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🗄️ Database

The initial database will contain four main entities:

```text
Users
  │
  │ 1:N
  ▼
Orders
  │
  │ 1:N
  ▼
OrderItems
  │
  │ N:1
  ▼
Books
```

### Users

```text
id
name
email
password_hash
created_at
```

### Books

```text
id
title
author
description
price
stock
created_at
```

### Orders

```text
id
user_id
status
total_price
created_at
```

### Order Items

```text
id
order_id
book_id
quantity
price
```

---

## 🔌 API Endpoints

### Users

```http
POST   /users
GET    /users
GET    /users/{id}
DELETE /users/{id}
```

### Books

```http
POST   /books
GET    /books
GET    /books/{id}
PUT    /books/{id}
DELETE /books/{id}
```

### Orders

```http
POST /orders
GET  /orders
GET  /orders/{id}
GET  /users/{id}/orders
```

### Authentication

Planned:

```http
POST /auth/register
POST /auth/login
GET  /auth/me
```

---

## 🤖 AI Agent — Future Feature

The AI component will be added after the core API is complete.

The agent will act as a **book assistant** and use tools exposed by the backend.

For example:

```text
User
 │
 ▼
┌──────────────────┐
│   Book Assistant │
│      Agent       │
└────────┬─────────┘
         │
         ├── search_books()
         ├── get_book()
         ├── check_stock()
         └── recommend_books()
                  │
                  ▼
             FastAPI API
                  │
                  ▼
             PostgreSQL
```

Example conversation:

```text
User:
I want a fantasy book under €20.

Agent:
Sure! I found 5 fantasy books under €20.
Would you like something classic, modern, or beginner-friendly?
```

## Installation
Right only basic functionality has been implemented
In order to see what's going on do the following:
1. Close the repo: git clone https://github.com/GeorgiosMavropoulos/IntelligentBookAPI.git
2. Navigate to repo folder
3. Install uv uvicorn
4. Initialize uv: uv init
5. Create venv: uv venv
6. Activate venv
7. Install fastapi: uv add fastapi
8. Install sqlalchemy: uv add sqlalchemy




The agent should rely on **real data from the bookstore backend** rather than having book information hardcoded into the prompt.

---

## 🧪 Testing

Tests will cover:

* User creation
* User authentication
* Book CRUD
* Order creation
* Stock management
* Invalid requests
* Authentication/authorization
* Database relationships

Run tests with:

```bash
pytest
```

---

## 🐳 Running with Docker

Start the application and PostgreSQL:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI interactive documentation:

```text
http://localhost:8000/docs
```

Alternative documentation:

```text
http://localhost:8000/redoc
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/bookstore

JWT_SECRET=change-me
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Never commit `.env` to Git.

Use `.env.example` instead.

---

## 🗺️ Roadmap

* [ ] Project setup
* [ ] FastAPI application
* [ ] PostgreSQL connection
* [ ] SQLAlchemy models
* [ ] Alembic migrations
* [ ] Books CRUD
* [ ] Users CRUD
* [ ] Orders
* [ ] Relationships
* [ ] JWT authentication
* [ ] Authorization / roles
* [ ] Pagination
* [ ] Search & filtering
* [ ] Transactions
* [ ] Tests
* [ ] Docker
* [ ] AI Book Agent
* [ ] Agent tools
* [ ] Natural-language book search
* [ ] Book recommendations

---

## 💡 Why this project?

This project is intentionally small enough to finish, but large enough to practice concepts that appear in real backend applications.

The final goal is to have:

**FastAPI + PostgreSQL + Authentication + Docker + Tests + AI Agent**

without starting with the AI part before the backend foundation is solid.

---

## 📌 Status

🚧 **In development**

Currently focusing on the core FastAPI + PostgreSQL backend.

The AI Book Agent will be added in a later phase.
