from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.secret_key = "........"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/connect")
def connect():
	return render_template("base.html")

@app.route("/ct/2228j8jd298jd28h938h2d9j928kdi29h3hjdbsjcnss/ew489n3993nbfkjs4lw")
def send():
	return render_template("msgSent.html")

@app.route("/bk1")
def book1():
	return render_template("bk1.html")

@app.route("/bk2")
def book2():
	return render_template("bk2.html")

@app.route("/bk3")
def book3():
	return render_template("bk3.html")

@app.route("/bk4")
def book4():
	return render_template("bk4.html")

@app.route("/bk5")
def book5():
	return render_template("bk5.html")

@app.route("/bk6")
def book6():
	return render_template("bk6.html")

@app.route("/bk7")
def book7():
	return render_template("bk7.html")


if __name__ == '__main__':
	app.run(debug=True)