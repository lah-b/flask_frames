from flask import Flask, render_template, request, jsonify

from .web3_test import is_w3_connected
from .web3_qn import get_tx_data
from .abi import abi

app = Flask(__name__)


@app.route("/")
def home():
    w3_response = is_w3_connected()
    return render_template("homePage.html", name="Dawg", w3_connect=w3_response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/mint-post", methods=["POST"])
def mint_post():
    post_data = request.json
    print("NICE CLICK")
    print(post_data)
    user_acct = post_data["untrustedData"]["address"]
    print(user_acct + " IS THE ADDRESS")
    tx_data = get_tx_data(user_acct)
    print(tx_data + " IS THE TX DATA")
    data = {
        "chainId": "eip155:8453",
        "method": "eth_sendTransaction",
        "params": {
            "abi": abi(),
            "to": "0xD09d72031Ce8212efD8928F1A3814E7F8da0fDfD",
            "data": tx_data,
        },
    }
    return jsonify(data), 200


@app.route("/mint-post-callback", methods=["POST"])
def mint_post_callback():
    post_data = request.json
    print(post_data)
    tx_hash = post_data["untrustedData"]["transactionId"]

    return render_template("frame2.html", tx_hash=tx_hash), 200
