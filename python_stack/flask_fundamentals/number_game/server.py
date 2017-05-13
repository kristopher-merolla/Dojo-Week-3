from flask import Flask, render_template, request, redirect, session

import random # import the random module

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/too_low')
def too_low():
	session.pop('input_num')
	session.pop('computer_num')
	return render_template("too_low.html")

@app.route('/too_high')
def too_high():
	session.pop('input_num')
	session.pop('computer_num')
	return render_template("too_high.html")

@app.route('/won')
def won():
	session.pop('input_num')
	session.pop('computer_num')
	return render_template("correct_guess.html")

@app.route('/user_input', methods=['POST'])
def button():
	print "Button clicked"
	session['input_num'] = int(request.form['input_num'])
	session['computer_num'] = random.randrange(1, 100) # random number between 1 and 100
	print session['input_num']
	print "computer number:",session['computer_num']
	if (session['computer_num'] == session['input_num']):
		print "You Won!"
		return redirect('/won')
	if (session['computer_num'] < session['input_num']):
		print "Too High!"
		return redirect('/too_high')
	if (session['computer_num'] > session['input_num']):
		print "Too Low!"
		return redirect('/too_low')

app.run(debug=True)
