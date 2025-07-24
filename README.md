# 📝 Blog App — React + FastAPI

A **full-stack blog application** built with **React (Vite)** and **FastAPI**, supporting full **CRUD operations**, responsive UI with **Bootstrap**, and **SQLite** for persistent data storage. Clean architecture and RESTful design.

---

## 📁 Project Structure

```
project-root/
│
├── backend/               # FastAPI backend
│   ├── alembic/           # Alembic migrations
│   ├── app/               # Core FastAPI application
│   │   ├── crud.py        # DB operations
│   │   ├── database.py    # DB setup
│   │   ├── main.py        # FastAPI app entry point
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── routes.py      # API routes
│   │   ├── schemas.py     # Pydantic schemas
│   │   └── seed.py        # Optional DB seed script
│   ├── blog.db            # SQLite database
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # React frontend (Vite)
│   ├── public/            # Static files
│   ├── src/
│   │   ├── assets/        # Images & styling
│   │   ├── components/    # Reusable components (Navbar, BlogList)
│   │   ├── pages/         # Page views (CreatePost, BlogDetail)
│   │   ├── App.jsx        # Main app component
│   │   └── main.jsx       # React entry point
│   ├── index.html         # Base HTML file
│   ├── package.json       # JS dependencies
│   └── vite.config.js     # Vite config
│
└── .gitignore             # Ignored files for Git
```

---

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) blog posts
- ✅ RESTful API with FastAPI
- ✅ React frontend built with Vite
- ✅ Responsive UI using Bootstrap
- ✅ SQLite for lightweight storage
- ✅ Clean separation of frontend and backend

---

## 📦 Tech Stack

| Frontend       | Backend       | Database | Styling   | Others       |
|----------------|----------------|----------|-----------|--------------|
| React (Vite)   | FastAPI        | SQLite   | Bootstrap | Axios, Alembic |

---

## ⚙️ Getting Started

### 1. 🔥 Backend Setup

```bash
cd backend
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. ⚡ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

- Frontend runs on: `http://localhost:5173`
- Backend runs on: `http://localhost:8000`

---

## 🧪 Example Routes (FastAPI)

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/blogs`         | Fetch all blog posts   |
| GET    | `/blogs/{id}`    | Get a single post      |
| POST   | `/blogs`         | Create a blog post     |
| PUT    | `/blogs/{id}`    | Update a blog post     |
| DELETE | `/blogs/{id}`    | Delete a blog post     |

---

## ❌ .gitignore Highlights

Make sure the following are ignored:

```
# Python
env/
__pycache__/
*.pyc
*.db

# Node
node_modules/
dist/

# General
*.log
.DS_Store
```

---

## 📸 Screenshots (Optional)

> 💡 Add screenshots of your frontend UI to visually showcase your app!

---

## ✨ Future Improvements

- Add user authentication (JWT)
- Markdown support for blog content
- Image upload with cloud storage
- Pagination for large posts
- Deploy with Docker

---

## 🤝 License

This project is open-source and available under the [MIT License](LICENSE).
