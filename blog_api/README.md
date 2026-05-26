# Blog API Service using Django & GraphQL

## Overview

This project is a Blog API Service built using Django, GraphQL, and SQLite. It supports CRUD operations for blog posts and comments using GraphQL queries and mutations.

---

## Tech Stack

- Python
- Django
- GraphQL
- Graphene-Django
- SQLite

---

## Features

### Post Operations
- Create Post
- Update Post
- List Posts
- Get Single Post

### Comment Operations
- Create Comment
- Delete Comment
- View Comments for a Post

---

## Project Structure

```text
Assignment/
│
├── blog/
│   ├── models.py
│   ├── schema.py
│   ├── admin.py
│
├── blogproject/
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
├── graphql_queries.md
├── README.md
```

---

## Setup Instructions

### Install Dependencies

```bash
pip install django
pip install graphene-django
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## URLs

### GraphQL Endpoint

```text
http://127.0.0.1:8000/graphql/
```

### Admin Panel

```text
http://127.0.0.1:8000/admin/
```

---

## Database Models

### Post
- title
- description
- publish_date
- author

### Comment
- post (ForeignKey)
- text
- author

One Post can have multiple Comments.

---

## Example Query

```graphql
{
  posts {
    id
    title
    author
  }
}
```

---

## Example Mutation

```graphql
mutation {
  createPost(
    title: "First Post",
    description: "Hello GraphQL",
    publishDate: "2026-05-22",
    author: "Alice"
  ) {
    post {
      id
      title
      author
    }
  }
}
```

---

## Request Flow

```text
GraphiQL
→ GraphQL Schema
→ Django ORM
→ SQLite Database
→ JSON Response
```

---

## Key Concepts Used

- GraphQL Queries & Mutations
- CRUD Operations
- Django ORM
- SQLite Database
- ForeignKey Relationships

---

## Author

Poornima P
