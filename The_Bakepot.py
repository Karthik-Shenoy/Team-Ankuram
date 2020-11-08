from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	return

@app.route("/shop")
def shopPage():
	return render_template("shop.html")

@app.route("/Contact-Us")
def contactPage():
	return render_template("Contact_US.html")

@app.route("/contribute")
def contribute():
	return render_template("contribute.html")

if __name__ == "__main__":
	app.run(debug = True)


