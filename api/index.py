from flask import Flask, render_template

# from web3_test import is_w3_connected

app = Flask(__name__)


@app.route("/")
def home():
    print("hello world!!!!")
    # print(f"Is web3 connected {is_w3_connected()}")
    return render_template("homePage.html")


@app.route("/about")
def about():
    return "About"
