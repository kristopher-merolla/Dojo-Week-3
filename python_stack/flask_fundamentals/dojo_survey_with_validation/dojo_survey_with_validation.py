from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

@app.route('/')
def landing_page():
	return render_template("index.html") #setting landing page as our form page


@app.route('/users', methods=['POST']) #method for posting a form, redirect back to home page (or any other page!)
def users():
	name = request.form['name']
	location = request.form['location']
	comment = request.form['comment']
	language = request.form['language']

	if (len(name) == 0):
		# display an error for empty name field
		session['error'] = "<p style='color:red;'>Error, name field empty.  Please try again.</p>"
		return redirect('/')

	if (len(comment) == 0):
		# display an error for empty comment field
		session['error'] = "<p style='color:red;'>Error, comment field empty.  Please try again.</p>"
		return redirect('/')

	if (len(comment) > 120):
		#display an error for comment field > 120 characters
		session['error'] = "<p style='color:red;'>Error, comment field must be < 120 characters.  Please try again.</p>"
		return redirect('/')

	if (session.get('error')!= None):
		#blank out error message
		session['error'] = ""

	return render_template("result.html",name=name,location=location,language=language,comment=comment)

app.run(debug=True)