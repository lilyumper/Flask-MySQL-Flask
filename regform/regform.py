from flask import Flask, redirect, render_template, flash, request, url_for, session
import re
app= Flask(__name__)
app.secret_key= "yumper"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def root():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def post():
    print "shit"

    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1: 
        flash("Field cannot be blank","blankerror")
    elif len(request.form['last_name']) < 1 or len(request.form['password']) < 1:
        flash("Field cannot be blank","blankerror") 
    elif len(request.form['confirm']) <1:
        flash("Field cannot be blank","blankerror")
        
     
    elif request.form['password'] != request.form['confirm']:
        flash("Passwords don't match","passerror")
        print request.form['password']
        print request.form['confirm']
    elif re.search('[0-9]', request.form['password']) is None:
        flash("You need a number in the Password", "nope")
     
    elif re.search('[A-Z]', request.form['password']) is None:
        flash("You need an upper case letter in password", "nodice")
        

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address","emailerror")
        
    
    return redirect('/')

app.run(debug=True)
