from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_jwt_extended import *

app = Flask(__name__)
app.secret_key = 'ul88_babo'
app.permanent_session_lifetime = timedelta(minutes=5) # 5분마다 세션 초기화

# In-memory user database
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and check_password_hash(user['password'], password):
            session.permanent = True # 세션 추가
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists', 'danger')
        else:
            hashed_password = generate_password_hash(password)
            users[username] = {'password': hashed_password}
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route('/file_upload',  methods=['GET', 'POST'])
def file_upload():
    return render_template('file_upload.html')


if __name__ == '__main__':
    app.run(debug=True)
