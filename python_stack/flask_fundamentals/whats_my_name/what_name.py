from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template("index.html") #setting landing page as our form page


@app.route('/process')
def after_submit():
	return render_template("name_form.html")


@app.route('/users', methods=['POST']) #method for posting a form, redirect back to home page (or any other page!)
def users():
	name = request.form['name']
	print name
	return redirect("/")


app.run(debug=True)