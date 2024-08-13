
import os
from flask import Flask, flash, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import timedelta

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = 'ul88_babo'
app.permanent_session_lifetime = timedelta(minutes=5) # 5분마다 세션 초기화
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# In-memory user database
users = {}

def allowed_file(filename): # 파일 화이트 리스트 필터링
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
