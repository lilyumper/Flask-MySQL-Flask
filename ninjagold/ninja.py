from flask import Flask, redirect, render_template, request, session
import random
import datetime
app= Flask(__name__)
app.secret_key ="Yumper"

@app.route('/', methods=["GET","POST"])
def root():
    if session.get('money') is None:
        session['money'] = 0
    if session.get('log') is None:
        session['log'] = ''
    loot= session['money']
    info= session['log']
    return render_template('ninjagold.html',loot=loot,info=info)

@app.route('/process', methods=["POST"])
def process():

    fgold = random.randrange(10, 21)
    cgold = random.randrange(5,11)
    hgold = random.randrange(2,6)
    ccgold = random.randrange(0,51)
    
    
    if request.form['building'] == 'farm':
        session['money']+= fgold
        session['log'] ='You have found {} gold {}'.format(fgold,datetime)
    elif request.form['building'] =="cave":
        session['money']+=cgold
        session['log'] ='You have found {} gold {}'.format(cgold,datetime)
    elif request.form['building']== "house":
        session['money']+= hgold
        session['log'] ='You have found {} gold {}'.format(hgold,datetime)
    elif request.form['building'] =='casino':
        x = random.randrange(0,1)
        if x == 0:
            session['money']+= ccgold
            session['log'] ='You have found {} gold {}'.format(ccgold,datetime)
        else:
            if x ==1:
                session['money']-= ccgold
                session['log'] = "YOU GAMBLED TOO MUCH YOU LOST {} gold {}".format(ccgold,datetime)
    elif request.form['building'] == 'restart':
        session.pop('money')
        session.pop('log')
    return redirect('/') 

app.run(debug=True)
    
