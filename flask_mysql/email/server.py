from flask import Flask, request, redirect, render_template, session, flash, session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'userdb')
app.secret_key="sneakysneaky"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def dashboard():
    
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    data ={
        'email': request.form['email']
    }
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        return redirect("/")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        return redirect("/")
    else:
        mysql.query_db("INSERT INTO users(email, created_on, updated_on) Values(:email,NOW(),NOW())",data)
        return redirect("/success")

@app.route('/success')
def success():
    users = mysql.query_db("SELECT * FROM users")
    return render_template("success.html", users=users)

app.run(debug=True)
