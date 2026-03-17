
# DogHub 🐶

DogHub is a social playground for dog parents and their furry best friends.

With DogHub you can:

- 🐕 Create adorable profiles for your dogs
- 🌳 Discover nearby dog parks, trails, and off-leash areas
- 🐾 Find playmates and organize dog meetups
- 🍔 Explore pet-friendly restaurants and hangouts

Because every dog deserves more friends, more adventures, and more tail wags.
This repository contains:

- **Django + DRF backend**
- **React frontend**

---

# Project Structure

backend/
    Django REST API

frontend/
    React UI

---

# Prerequisites

Install:

- Python 3.10+
- Node.js 18+
- PostgreSQL

---

# Backend Setup (Django)

## 1️⃣ Navigate to backend

```bash
cd backend
```

## 2️⃣ Create virtual environment

Mac / Linux

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure environment variables

Create `.env` file inside `backend/`

Example:

```
DB_NAME=doghub
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

---

## 5️⃣ Run migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Start backend server

```bash
python manage.py runserver
```

Backend API runs at:

```
http://127.0.0.1:8000
```

Example APIs:

```
GET /api/dogs/
GET /api/parks/
GET /api/users/profile/
```

---

# Frontend Setup (React)

## 1️⃣ Navigate to frontend

```bash
cd frontend
```

## 2️⃣ Install dependencies

```bash
npm install
```

---

## 3️⃣ Start frontend

```bash
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

# Example Pages

Dog list  
Dog parks  

More features can be added:

• Dog meet posts  
• Dog food section  
• Pet-friendly restaurants  
• Dog park heatmap  

---

# Future Features

Planned modules:

```
posts/          dog meet posts
food/           dog food recipes
restaurants/    pet friendly restaurants
parks/          crowd heatmap
likes/          like system
comments/       comments
```
