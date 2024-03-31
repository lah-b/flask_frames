from flask import Flask, render_template, request, jsonify, make_response
from .mint_sepolia import get_tx_data
from .abi import sep_abi

app = Flask(__name__)


@app.route("/")
def home():
    page = render_template("homePage.html")
    resp = make_response(page)
    resp.headers["cache-control"] = "max-age=360"

    return resp


@app.route("/about")
def about():
    page = render_template("aboutPage.html")
    resp = make_response(page)
    resp.headers["cache-control"] = "max-age=360"
    return resp


@app.route("/sep-mint")
def sep_home():
    return render_template("sepMintFrame.html")


@app.route("/sep-mint-post", methods=["POST"])
def sep_mint_post():
    post_data = request.json
    user_acct = post_data["untrustedData"]["address"]

    tx_data = get_tx_data(user_acct)
    data = {
        "chainId": "eip155:84532",
        "method": "eth_sendTransaction",
        "params": {
            "abi": sep_abi(),
            "to": "0x40eA87a0DffaD828778EB248156DF01A358f541b",
            "data": tx_data,
        },
    }
    return jsonify(data), 200


@app.route("/sep-mint-post-callback", methods=["POST"])
def sep_mint_post_callback():
    post_data = request.json
    print(post_data)
    tx_hash = post_data["untrustedData"]["transactionId"]
    return render_template("sepScanFrame.html", tx_hash=tx_hash), 200


@app.route("/gh")
def gh():
    return render_template("ghFrame.html")
