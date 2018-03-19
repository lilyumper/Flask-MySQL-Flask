from flask import Flask, render_template, url_for, request, flash, session, redirect
app = Flask(__name__)
app.secret_key = "Keystuff"

@app.route('/', methods= ['GET'])
def root():
    return render_template ("index.html")

@app.route('/submit', methods= ['POST'])
def submit():
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form["comment"]
    if len(request.form['name']) <1:
        flash("Name cannot be empty")
        return redirect('/')
    if len(request.form['comment']) >126:
        flash("Comment cannot be over 126 characters")
        return redirect('/')
    else:
        return render_template("submit.html",name=name, dojo=dojo,language=language,comment=comment)

app.run(debug=True)
