#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, name TEXT, balance REAL)''')
        conn.commit()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    balance = float(request.form['balance'])
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, balance) VALUES (?, ?)', (name, balance))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_balance/<int:user_id>', methods=['POST'])
def update_balance(user_id):
    new_balance = float(request.form['balance'])
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
