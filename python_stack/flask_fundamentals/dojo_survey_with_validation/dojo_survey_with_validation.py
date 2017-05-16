from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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
		# display an error
		return redirect('/')

	if (len(comment) == 0):
		# display an error
		return redirect('/')

	if (len(comment) > 120):
		#display an error
		return redirect('/')

	return render_template("result.html",name=name,location=location,language=language,comment=comment)

app.run(debug=True)