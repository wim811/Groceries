from flask import Flask, render_template, request, url_for



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/boodschappenlijst", methods=["GET","POST"])
def boodschappenlijst():

    return render_template("boodschappenlijst.html", title="Boodschappenlijst")

@app.route("/onderhoud", methods=["GET","POST"])
def onderhoud():

    return render_template("onderhoud.html", title="Onderhoud")

if __name__ == "__main__":
    app.run(debug=True)

