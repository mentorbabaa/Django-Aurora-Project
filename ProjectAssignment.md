# 📝 Assignment: Build a Flask ToDo App with Amazon Aurora MySQL

## 🎯 Objective

Your task is to build a **ToDo web application** using **Python Flask** as the backend and **HTML/CSS/JavaScript** as the frontend. The application must connect to an **Amazon Aurora MySQL** database and utilize **separate read and write endpoints** for optimized database access.

---

## 📚 Overview

This project aims to test your skills in:

- Backend web development with Flask
- Frontend design with HTML/CSS/JavaScript
- Working with Amazon Aurora MySQL
- Environment variable configuration
- Logging and debugging cloud services
- Building a complete end-to-end web app

---

## 📌 Features to Implement

1. **Frontend**
   - A simple web interface to:
     - List all existing todo items
     - Add new todo items
     - Delete existing todo items

2. **Backend**
   - Flask server with the following routes:
     - `GET /` - Display all todos (read endpoint)
     - `POST /add` - Add a new todo (write endpoint)
     - `GET /delete/<id>` - Delete a todo (write endpoint)

3. **Database**
   - Use **Amazon Aurora MySQL**
   - Create a table:
     ```sql
     CREATE TABLE todos (
         id INT AUTO_INCREMENT PRIMARY KEY,
         content VARCHAR(255) NOT NULL
     );
     ```

4. **Aurora Endpoints**
   - Use **Writer endpoint** for inserts and deletes
   - Use **Reader endpoint** for fetching todos

5. **Logging**
   - Print logs to indicate which endpoint (read/write) is being used in each DB operation

---

## 📦 Deliverables

Push the following to your GitHub repository:

```
/your-project
│
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend template
├── static/
│   └── style.css            # (Optional) Styling
├── README.md                # Project overview and assignment instructions
├── solution.md              # Step-by-step solution guide
└── .env (optional)          # Environment variables (exclude from public repo)
```

---

## 🧪 Testing Criteria

✅ You should be able to:

- Add a task
- View tasks
- Delete a task
- Verify logs show proper read/write endpoint usage
- Restart server and see data persisted (Aurora is connected)

---

## 🛠 Tech Stack

- Python 3
- Flask
- MySQL (Aurora)
- HTML/CSS/JavaScript
- AWS (Aurora, EC2/local)

---

## 🌐 Environment Configuration

Ensure the following environment variables are set:

```bash
export AURORA_WRITE_ENDPOINT=<your-writer-endpoint>
export AURORA_READ_ENDPOINT=<your-reader-endpoint>
export DB_USER=<your-db-username>
export DB_PASSWORD=<your-db-password>
export DB_NAME=todo_app
```

---

## ⏳ Timeline

Suggested time to complete: **4-6 hours**

---

## 🏁 Submission

- Submit your GitHub repo link containing all required files.
- Include a working screenshot or video demo (optional but encouraged).
- Make sure logs are visible in the console for DB endpoint usage.

---

## 🙌 Bonus (Optional)

- Add Bootstrap or Tailwind for styling
- Add AJAX for add/delete without page reload
- Deploy the app on EC2 or render.com

---

Good luck! 🚀
