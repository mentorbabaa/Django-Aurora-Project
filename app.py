# app.py
from flask import Flask, render_template, request, redirect, jsonify
import pymysql
import os
from dotenv import load_dotenv
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

load_dotenv()
# Aurora Endpoints
DB_WRITE_HOST = os.environ.get('AURORA_WRITE_ENDPOINT')
DB_READ_HOST = os.environ.get('AURORA_READ_ENDPOINT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

def get_connection(read=False):
    host = DB_READ_HOST if read else DB_WRITE_HOST
    endpoint_type = "READ" if read else "WRITE"
    logging.info(f"Using {endpoint_type} endpoint: {host}")
    return pymysql.connect(
        host=host,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    conn = get_connection(read=True)
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM todos ORDER BY id DESC")
        todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO todos (content) VALUES (%s)", (content,))
            conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM todos WHERE id=%s", (todo_id,))
        conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
