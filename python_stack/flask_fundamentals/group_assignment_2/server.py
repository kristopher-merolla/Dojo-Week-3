from flask import Flask, render_template, request, redirect, session

import random # import the random module

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
	if (session.get('win')==None): # if the count = None, set count to 0 (this is useful for our first navigation to /)
		session['win'] = 0
	if (session.get('draw')==None): # if the count = None, set count to 0 (this is useful for our first navigation to /)
		session['draw'] = 0
	if (session.get('loss')==None): # if the count = None, set count to 0 (this is useful for our first navigation to /)
		session['loss'] = 0
	if (session.get('comp_throw_name') == None):
		session['comp_throw_name'] = "Pick a button below to throw a rock, paper, or scissor at the computer!"
	# if (session.get('result') == None):
	# 	session['result']

	return render_template("index.html")


@app.route('/button', methods=['POST'])
def button():
	session['comp_throw'] = random.randrange(0, 3) # random number between 0-2
	#0 = rock, 1 = paper, 2 = scissors
	print session['comp_throw']
	session['button_press'] = request.form['button_press']

	if (session['button_press'] == 'rock'): # user throws rock
		if (session['comp_throw'] == 0):
			session['comp_throw_name'] = "The computer threw rock against your"
			session['draw'] += 1
			session['result'] = "which is a draw"
		elif (session['comp_throw'] == 1):
			session['comp_throw_name'] = "The computer threw paper against your"
			session['loss'] += 1
			session['result'] = "which is a loss"
		else:
			session['comp_throw_name'] = "The computer threw scissors against your"
			session['win'] += 1
			session['result'] = "which is a win"

	elif (session['button_press'] == 'paper'):  # user throws paper
		if (session['comp_throw'] == 0):
			session['comp_throw_name'] = "The computer threw rock against your"
			session['win'] += 1
			session['result'] = "which is a win"
		elif (session['comp_throw'] == 1):
			session['comp_throw_name'] = "The computer threw paper against your"
			session['draw'] += 1
			session['result'] = "which is a draw"
		else:
			session['comp_throw_name'] = "The computer threw scissors against your"
			session['loss'] += 1
			session['result'] = "which is a loss"

	elif (session['button_press'] == 'scissors'):  # user throws scissors
		if (session['comp_throw'] == 0):
			session['comp_throw_name'] = "The computer threw rock against your"
			session['loss'] += 1
			session['result'] = "which is a loss"
		elif (session['comp_throw'] == 1):
			session['comp_throw_name'] = "The computer threw paper against your"
			session['win'] += 1
			session['result'] = "which is a win"
		else:
			session['comp_throw_name'] = "The computer threw scissors against your"
			session['draw'] += 1
			session['result'] = "which is a draw"

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['win'] = 0
	session['loss'] = 0
	session['draw'] = 0
	session['comp_throw_name'] = "Play again?  Just click a button below!"
	session['result'] = ""
	session['button_press'] = ""

	return redirect('/')



app.run(debug=True)
