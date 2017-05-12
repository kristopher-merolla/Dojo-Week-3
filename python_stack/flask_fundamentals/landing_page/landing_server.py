from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template("index.html")


@app.route('/ninjas')
def ninja_page():
	return render_template("ninjas.html")


@app.route('/dojos/new')
def dojo_form():
	return render_template("dojos.html")


@app.route('/users', methods=['POST']) #method for posting a form, redirect back to home page (or any other page!)
def users():
	return redirect("/")


app.run(debug=True)