# 📚 Intelligent Bookstore API

A **Bookstore REST API** built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy 2.0**, designed as a realistic backend project and as the foundation for a future **AI Book Agent**.

The project is being developed incrementally, starting with a clean and reliable backend before introducing the LLM/AI layer.

---

## 🚀 Tech Stack

* **FastAPI** — REST API
* **PostgreSQL** — relational database
* **SQLAlchemy 2.0** — ORM
* **Pydantic** — request/response validation
* **Alembic** — database migrations
* **uv** — Python package and environment management
* **Pytest** — testing
* **Docker / Docker Compose** — planned development/deployment environment
* **LLM / AI Agent** — next development phase

---

# 📌 Current Status

🚧 **In development**

The core bookstore backend is currently being implemented.

### Completed so far

* FastAPI application setup
* PostgreSQL database connection
* SQLAlchemy models
* Pydantic schemas
* Service layer
* Router layer
* Book CRUD
* Publisher CRUD
* Author CRUD
* Book ↔ Author many-to-many relationship
* Foreign-key validation
* Duplicate resource validation
* Centralized custom exception handling
* HTTP status codes for application errors
* Pagination parameters for collection endpoints
* Basic API responses with success messages and data

The next major milestone is the **LLM / AI Book Agent**.

---

# 🏗️ Current Architecture

The application follows a layered structure:

```text
                    ┌─────────────────┐
                    │     Client      │
                    │   / Postman     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │     Routers     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Services     │
                    │ Business Logic  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   SQLAlchemy    │
                    │      ORM        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    └─────────────────┘
```

The future AI layer will interact with the backend through dedicated tools rather than directly manipulating the database.

---

# 📚 Current Domain Model

The current bookstore domain contains:

```text
Publisher
    │
    │ 1:N
    ▼
  Books
    │
    │ N:M
    ▼
 Authors
```

A book belongs to a publisher and can have multiple authors.

An author can be associated with multiple books.

The many-to-many relationship is represented through an association table:

```text
Books
  │
  │
  ▼
BookAuthors
  ▲
  │
  │
Authors
```

---

# 📁 Project Structure

The project is organized into separate layers for routing, business logic, database models, schemas, and exceptions.

```text
IntelligentBookAPI/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── book_routes/
│   │   ├── publisher_routes/
│   │   ├── author_routes/
│   │   └── authors_books_routes/
│   │
│   ├── services/
│   │   ├── book_service.py
│   │   ├── publisher_service.py
│   │   ├── author_service.py
│   │   └── authors_books_service.py
│   │
│   ├── models/
│   │   ├── book_model.py
│   │   ├── publisher_model.py
│   │   ├── author_model.py
│   │   └── book_authors_model.py
│   │
│   ├── schemas/
│   │   ├── book_schema.py
│   │   ├── publisher_schema.py
│   │   ├── author_schema.py
│   │   └── book_authors_schema.py
│   │
│   ├── exceptions/
│   │   ├── base_exception_class.py
│   │   ├── book_exceptions/
│   │   ├── publisher_exceptions/
│   │   ├── author_exceptions/
│   │   └── authors_books_exceptions/
│   │
│   └── database/
│       └── database.py
│
├── alembic/
│
├── tests/
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

---

# 🔌 Current API

## Books

```http
POST   /books/
GET    /books/
GET    /books/{book_id}
PUT    /books/{book_id}
DELETE /books/{book_id}
```

Books currently support validation for:

* Existing publisher
* Unique ISBN
* Partial updates
* Missing books
* Publisher validation during updates

---

## Publishers

```http
POST   /publishers/
GET    /publishers/
GET    /publishers/{publisher_id}
GET    /publishers/name/{publisher_name}
PUT    /publishers/{publisher_id}
DELETE /publishers/{publisher_id}
```

Publisher validation includes:

* Duplicate publisher names
* Missing publishers
* Duplicate names during updates

---

## Authors

```http
POST   /authors/
GET    /authors/
GET    /authors/{author_id}
GET    /authors/name/{author_name}
PUT    /authors/{author_id}
DELETE /authors/{author_id}
```

Author validation includes:

* Duplicate authors
* Missing authors
* Duplicate names during updates

---

## Book ↔ Author Relationships

```http
POST   /authors_books/
GET    /authors_books/
GET    /authors_books/author/{author_id}
GET    /authors_books/book/{book_id}
DELETE /authors_books/{book_id}/{author_id}
```

The relationship layer validates:

* Author existence
* Book existence
* Duplicate relationships
* Missing relationships during deletion

---

# ⚠️ Error Handling

The API uses custom application exceptions instead of scattering `HTTPException` logic throughout the services.

The application contains a base exception:

```text
ExceptionServiceHandler
```

Domain-specific exceptions inherit from it.

Examples include:

```text
DuplicateAuthor
AuthorNotFound
DuplicatePublisher
PublisherNotFound
DuplicateISBN
BookNotFound
DuplicateAuthorBookEntry
```

Exceptions are converted into consistent JSON responses through a centralized FastAPI exception handler.

Example response:

```json
{
  "status": "error",
  "code": "Duplicate author",
  "message": "There is another author registered with that name"
}
```

This keeps the service layer focused on business logic while the exception handler is responsible for the HTTP response.

---

# 🗄️ Database

The current database contains the following core entities:

```text
Publishers
    │
    │ 1:N
    ▼
Books
    │
    │ N:M
    ▼
Authors
```

### Books

```text
id
title
year
isbn
price
description
genre
language
stock
publisher_id
created_at
updated_at
```

### Publishers

```text
id
publisher
```

### Authors

```text
id
author
```

### BookAuthors

```text
book_id
author_id
```

The database uses constraints such as foreign keys and uniqueness constraints to maintain data integrity.

---

# 🤖 Next Phase — LLM Book Agent

The next major ticket is the **LLM Book Agent**.

The goal is **not** to hardcode bookstore information into the LLM prompt.

Instead, the LLM should use tools that communicate with the existing bookstore backend.

For example:

```text
                         User
                           │
                           ▼
                  ┌─────────────────┐
                  │   Book Agent    │
                  │      LLM        │
                  └────────┬────────┘
                           │
                    Tool / Function Calls
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
       search_books()  get_book()   check_stock()
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     FastAPI API
                           │
                           ▼
                      PostgreSQL
```

The agent should be able to answer questions using **real-time data from the bookstore backend**.

Example questions:

> "Do you have any books by Tolkien?"

> "Which fantasy books are under €20?"

> "Is The Hobbit currently in stock?"

> "Tell me about Dune."

> "What books do you have by Stephen King?"

> "Recommend a fantasy book under €20."

---

# 🧠 Planned AI Tools

The initial tool set may include:

```text
search_books()
get_book()
get_books_by_author()
get_books_by_genre()
check_book_stock()
get_books_by_price()
```

The exact tool design will be decided during the LLM phase.

The important architectural principle is:

**The LLM should reason and decide which tool to use, while the backend remains responsible for retrieving and validating bookstore data.**

---

# 🧪 Testing

Testing is planned for the core API and will eventually cover:

* Book CRUD
* Publisher CRUD
* Author CRUD
* Book-author relationships
* Duplicate resources
* Missing resources
* Invalid requests
* Database constraints
* Authentication
* Authorization
* Orders
* AI tools

Run tests with:

```bash
pytest
```

---

# 🐳 Docker

Docker / Docker Compose is planned for the development environment.

The target setup will run:

```text
FastAPI
   │
   ▼
PostgreSQL
```

with a future AI/LLM integration layer.

---

# ⚙️ Environment Variables

Create a `.env` file for local configuration.

Example:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/bookstore

JWT_SECRET=change-me
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Never commit `.env` to Git.

Use `.env.example` for shared configuration templates.

---

# 🗺️ Roadmap

## Phase 1 — Core Backend

* [x] FastAPI application
* [x] PostgreSQL connection
* [x] SQLAlchemy models
* [x] Pydantic schemas
* [x] Books CRUD
* [x] Publishers CRUD
* [x] Authors CRUD
* [x] Book ↔ Author relationships
* [x] Basic validation
* [x] Custom exceptions
* [x] Centralized error handling

## Phase 2 — API Improvements

* [ ] Alembic migrations
* [ ] Automated tests
* [ ] Better response schemas
* [ ] Pagination improvements
* [ ] Search
* [ ] Filtering
* [ ] Sorting
* [ ] Transactions

## Phase 3 — Users & Authentication

* [ ] User model
* [ ] User CRUD
* [ ] Registration
* [ ] Password hashing
* [ ] JWT authentication
* [ ] Login
* [ ] Authentication dependencies
* [ ] User/admin roles
* [ ] Authorization

## Phase 4 — Orders

* [ ] Orders
* [ ] Order items
* [ ] Stock management
* [ ] Order transactions
* [ ] Order history

## Phase 5 — LLM / AI Book Agent 🤖

* [ ] LLM integration
* [ ] Tool/function calling
* [ ] Book search tool
* [ ] Book lookup tool
* [ ] Author search tool
* [ ] Stock tool
* [ ] Price/filter tool
* [ ] Natural-language search
* [ ] Book recommendations
* [ ] Agent conversation endpoint

## Phase 6 — Infrastructure

* [ ] Docker
* [ ] Docker Compose
* [ ] Production configuration
* [ ] CI/CD

---

# 💡 Project Goal

The project is intentionally being built incrementally.

The goal is to first create a reliable backend with a clear separation between:

```text
Routes
   ↓
Services
   ↓
Database
```

and then introduce the AI layer on top of that foundation.

The final architecture aims to combine:

**FastAPI + PostgreSQL + SQLAlchemy + Authentication + Testing + Docker + LLM Agent**

without allowing the AI layer to become responsible for core business logic or database integrity.

---

## 📌 Status

🚧 **In development**

**Current focus:** Core backend and error handling.

**Next ticket:** 🤖 **LLM / AI Book Agent**
