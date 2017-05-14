from flask import Flask, render_template, request, redirect, session

import random # import the random module

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
	if (session.get('gold_amt') == None):
		session['gold_amt'] = 0 #sets starting gold amount at 0

	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
	print "Money Processed"

	session['building'] = request.form['building']

	if (session['building'] == 'farm'):
		roll = random.randrange(10, 20)
		session['gold_amt'] += roll
		activity = "Earned "+str(roll)+" gold from the farm!"
		print activity

	if (session['building'] == 'cave'):
		roll = random.randrange(5, 10)
		session['gold_amt'] += roll
		activity = "Earned "+str(roll)+" gold from the cave!"
		print activity

	if (session['building'] == 'house'):
		roll = random.randrange(2, 5)
		session['gold_amt'] += roll
		activity = "Earned "+str(roll)+" gold from the house!"
		print activity

	if (session['building'] == 'casino'):
		roll = random.randrange(-50, 50)
		session['gold_amt'] += roll
		if (roll >= 0):
			activity = "Earned "+str(roll)+" gold from the casino! You're lucky!"
		if (roll < 0):
			activity = "Lost "+str(roll)+" gold from the casnio! Better luck next time..."
		print activity

	return redirect('/')

app.run(debug=True)












