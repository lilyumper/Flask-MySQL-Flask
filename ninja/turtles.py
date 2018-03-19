from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')
@app.route('/turtles')
def first():
    x ="tmnt.png"

    return render_template('turtles.html',x=x)

@app.route('/turtles/<color>')
def turtle(color):
    x ="tmnt.png"
    if color =="blue":
        x="leonardo.jpg"
    elif color == "red":
        x ="raphael.jpg"
    elif color =="purple":
        x= "donatello.jpg"
    elif color =="orange":
        x ="michelangelo.jpg"
    else:
        x ="notapril.jpg"
        
    return render_template("turtles.html",x=x)

app.run(debug=True)