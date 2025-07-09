# ✅ Solution Guide: Flask + Aurora ToDo App

This document outlines the complete solution to building and deploying a Flask ToDo App connected to Amazon Aurora MySQL.

---

### 🔧 Step-by-Step Implementation

#### 1. Aurora DB Setup
- Go to AWS Console → RDS → Create database
- Select Amazon Aurora → MySQL Compatible
- Enable writer and at least one reader instance
- Create a DB called `todo_app`
- Note the writer and reader endpoints

```sql
CREATE DATABASE todo_app;
USE todo_app;
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(255) NOT NULL
);
```

---

#### 2. Python Environment Setup
- Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
- Install dependencies:
```bash
pip install flask pymysql python-dotenv
```

---

#### 3. Configure Environment Variables
- Create a `.env` file:
```env
AURORA_WRITE_ENDPOINT=<your-writer-endpoint>
AURORA_READ_ENDPOINT=<your-reader-endpoint>
DB_USER=<your-db-user>
DB_PASSWORD=<your-db-password>
DB_NAME=todo_app
```
- Load these in your `app.py` using `os.environ.get()`

---

#### 4. Build the Flask App (`app.py`)
- Define routes `/`, `/add`, `/delete/<id>`
- Use a `get_connection(read=False)` method to toggle between endpoints
- Add logging to print whether `READ` or `WRITE` endpoint is being used

---

#### 5. Frontend (`templates/index.html`)
- Create a simple HTML form and list todos
- Link the form to `/add` and each item to `/delete/<id>`

---

#### 6. Run & Test
```bash
python3 app.py
```
- Go to `http://localhost:5000`
- Add and delete todos
- Check console logs to verify which endpoint was used

---

#### ✅ Verification
- Data persists after restart → Aurora DB is working
- Write logs show `WRITE` endpoint
- Read logs show `READ` endpoint

---

🎉 You now have a complete full-stack cloud-native ToDo app using Flask and Aurora!


## Incase you want to containerize your app 

### 🛠️ Step 1: Build the Docker image
In your terminal, navigate to your project folder and run:

docker build -t flask-todo-app .


### 🚀 Step 2: Run the container
 when running the container:


docker run -d -p 5000:5000 flask-todo flask-todo-app
