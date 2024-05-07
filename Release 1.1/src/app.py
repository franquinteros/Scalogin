from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect  
from flask_login import LoginManager, login_user, logout_user, login_required
 
from config import config

app = Flask (__name__)

@app.route ('/')
def index():
    return redirect(url_for('login'))
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        print (request.form['username'])
        print (request.form['password'])
    else:
        return render_template('./auth/login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()