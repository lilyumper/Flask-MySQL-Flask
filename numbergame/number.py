from flask import Flask, redirect, render_template, url_for, request, session, Markup
import random
app= Flask(__name__)
app.secret_key= "Yumper"
@app.route('/', methods=["GET", "POST"])
def root():
    if session.get('number') is None:
        session['number'] = random.randrange(0,101)
    message = ''
    color = ''
    button = ''

    if request.method == 'POST':
        display =""
        guess = request.form['Guess']

        if int(guess) < session['number']:
            message= 'You are TOO LOW'
            color = 'blue'
        elif int(guess) > session['number']:
            message = 'You are TOO HIGH'
            color ='red'
        elif int(guess) == session['number'] :
            message ='YOU GUESSED RIGHT!!!!!!!!'+ str(session['number'])+ "Was the NUMBER!!!"
            color ='gold'
            button = Markup("<a href='/return' class ='button'>Start Over</a>")
    else:
        display= "hidden"
    return render_template("index.html",color = color, message = message, button = button)
        
@app.route('/return')
def back():
    session.pop('number')
    return redirect('/')

app.run(debug=True)



   
