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
    data = {
        "chainId": "eip155:10",
        "method": "eth_sendTransaction",
        "params": {
            "to": "0x00000000fcCe7f938e7aE6D3c335bD6a1a7c593D",
            "data": render_string,
            "value": "984316556204476",
        },
    }
    return jsonify({"name": f"your name is {render_string}"}), 200
