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

@app.route("/Cake-By-Flavour")
def cake_by_flavour():
	return render_template("cake_by_flavour.html")

@app.route("/Cake-By-Theme")
def cake_by_theme():
	return render_template("cake_by_theme.html")

@app.route("/newly-arrived")
def newly_arrived_cakes():
	return render_template("newly_arrived_cakes.html")

@app.route("/Cup-Cakes")
def Cup_Cake():
	return render_template("Cup_Cake.html")

if __name__ == "__main__":
	app.run(debug = True)


