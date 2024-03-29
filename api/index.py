from flask import Flask, render_template, request, jsonify

from .web3_test import is_w3_connected

app = Flask(__name__)


@app.route("/")
def home():
    w3_response = is_w3_connected()
    return render_template("homePage.html", name="Dawg", w3_connect=w3_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/mint-post", methods=["POST"])
def parse_request():
    post_data = request.json  # Assuming JSON data is posted
    # Process the post_data
    render_string = post_data["name"]
    return jsonify({"name": render_string})
