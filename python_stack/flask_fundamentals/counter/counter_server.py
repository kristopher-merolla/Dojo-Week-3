from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def index():
	if (session.get('count')==None): # if the count = None, set count to 0 (this is useful for our first navigation to /)
		session['count'] = 0
	else:
		session['count'] += 1 # if the count != None, add one to the count each time page is loaded
	return render_template("index.html")


@app.route('/button', methods=['POST'])
def button():
	button_press = request.form['button_press']
	print button_press
	if (button_press=='add2'):
		session['count'] += 1
	if (button_press=='reset'):
		session['count'] = 0

	print session.get('button_press')
	print session['count']
	return redirect('/')





app.run(debug=True)
