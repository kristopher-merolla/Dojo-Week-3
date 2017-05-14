from flask import Flask, render_template, request, redirect, session

import random # import the random module

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
	if (session.get('gold_amt') == None):
		session['gold_amt'] = 0
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
	print "Money Processed"

	session['building'] = request.form['building']

	if (session['building'] == 'farm'):
		print "Farmed!"
		roll = random.randrange(10, 20)
		session['gold_amt'] += roll
	if (session['building'] == 'cave'):
		print "Cave!"
		roll = random.randrange(5, 10)
		session['gold_amt'] += roll
	if (session['building'] == 'house'):
		print "House!"
		roll = random.randrange(2, 5)
		session['gold_amt'] += roll
	if (session['building'] == 'casino'):
		print "Casino!"
		roll = random.randrange(-50, 50)
		session['gold_amt'] += roll

	return redirect('/')

app.run(debug=True)