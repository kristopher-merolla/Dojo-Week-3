from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def main_page():
  return render_template('index.html')    # Render the template and return it!

@app.route('/left')
def left_door():
	return render_template('left.html')    # Render the template and return it!


@app.route('/right') 
def right_door():
	return render_template('right.html')    # Render the template and return it!

@app.route('/red') 
def red_door():
	return render_template('red_door.html')    # Render the template and return it!

@app.route('/black') 
def black_door():
	return render_template('black_door.html')    # Render the template and return it!


app.run(debug=True)                       # Run the app in debug mode.