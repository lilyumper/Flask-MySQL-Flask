from flask import Flask, request, redirect, render_template, session, flash
import re
import md5
import os
import binascii
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'regdb')

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    login = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data ={'email':email}
    user = mysql.query_db(login,data)
    print user
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0].get('salt')).hexdigest()
    if user[0].get('hashed_password') == encrypted_password:
        print('valid combo')
        session['logged_in'] = user[0].get("id")
        print(session['logged_in'])
        return redirect('/success')
    else:
        flash('INVALID Password/Email Combination Please try again')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    errors = []
    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2 characters long")
        errors.append("First name must be at least 2 characters long")
    if re.search('[0-9]', request.form['first_name']) != None:
        flash("first name is letters only")
        errors.append("first name is letters only")
    if len(request.form['last_name']) < 2:
        flash("Last name must be at least 2 characters long")
        errors.append("Last name must be at least 2 characters long")
    if re.search('[0-9]', request.form['last_name']) != None:
        flash("last name is letters only")
        errors.append("Last name is letters only")
    if len(request.form['email']) < 1:
        flash("Email field must be filled")
        errors.append("Email field must be filled")
    elif EMAIL_REGEX.match(request.form['email']) == None:
        flash('invalid email formatting')
        errors.append('invalid email formatting')
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long") 
        errors.append("Password must be at least 8 characters long")
    if request.form['password'] != request.form['confirm_password']:
        flash("passwords do not match")  
        errors.append("passwords do not match")
    


    emailq="SELECT email FROM users"
    emailinfo=mysql.query_db(emailq)
    for i in emailinfo:
        if request.form['email']== i.get('email'):
            flash("Email is already in use")
            error.append("Duplicate Email")
            return redirect('/')
    
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()

    info = {
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'email':  email,
                'hashed_password':  hashed_pw,
                'salt': salt
                }

    reg= "INSERT INTO users (first_name, last_name, email, hashed_password, salt) VALUES(:first_name, :last_name,:email,:hashed_password,:salt)"

    mysql.query_db(reg,info)
    user="SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query = {'email': email}
    newuser = mysql.query_db(user,query)
    session['logged_in'] = newuser[0].get('id')
    print(session['logged_in'])
    return render_template('success.html')

@app.route('/success')
def success():
    return render_template('success.html')


app.run(debug=True)
