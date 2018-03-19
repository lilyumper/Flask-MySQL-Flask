from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'newfriends')


@app.route('/')
def dashboard():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", all_friends=friends)


@app.route('/submit', methods=["POST"])
def submit():
    data ={
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db("INSERT INTO friends (name,age,friend_since) VALUES (:name, :age, NOW())", data)
    return redirect("/")

app.run(debug="True")
