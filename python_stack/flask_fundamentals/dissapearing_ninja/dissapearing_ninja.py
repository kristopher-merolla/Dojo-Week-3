from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template("index.html") #setting landing page as our form page

@app.route('/ninja')
def all_turtle_page():
	return render_template("all_turtles.html")

@app.route('/ninja/blue')
def blue_turtle_page():
	return render_template("blue_turtle.html")

@app.route('/ninja/orange')
def orange_turtle_page():
	return render_template("orange_turtle.html")

@app.route('/ninja/red')
def red_turtle_page():
	return render_template("red_turtle.html")

@app.route('/ninja/purple')
def purple_turtle_page():
	return render_template("purple_turtle.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("not_april.html")

app.run(debug=True)