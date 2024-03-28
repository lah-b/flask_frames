from flask import Flask, render_template

from web3_test import is_w3_connected

app = Flask(__name__)


@app.route("/")
def home():
    w3_cnnected = is_w3_connected()
    return render_template("homePage.html", name="Dawg", w3_connect=w3_cnnected)


@app.route("/about")
def about():
    return "About"
