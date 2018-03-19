from flask import Flask, redirect, session, render_template, url_for, request
app= Flask(__name__)
app.secret_key = 'Yumper'
@app.route('/')
def root():
    if session.get('counter') is None:
      session['counter'] = -1
    
    session['counter'] +=1
    return render_template('counter.html')

@app.route('/submit', methods =['POST'])
def counter():
    return redirect('/')
@app.route('/plus', methods =['POST'])
def plus():
    session['counter'] +=1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():    
    session['counter']=-1
    return redirect('/')
app.run(debug=True)

