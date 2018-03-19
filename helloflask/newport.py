from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('root.html')

@app.route('/projects')
def projects():
    return render_template('myprojects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)