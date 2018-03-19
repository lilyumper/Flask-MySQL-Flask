from flask import Flask, url_for, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('color.html')

@app.route('/submit', methods = ["POST"])
def color():
    red = request.form["red"]
    green = request.form["green"]
    blue = request.form["blue"]
  
    
    return render_template('color.html',red=red, green=green,blue=blue)


app.run(debug=True)