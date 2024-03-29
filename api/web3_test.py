import os
# from web3 import Web3
# w3 = Web3(Web3.HTTPProvider("https://base-sepolia.g.alchemy.com/v2/pvnBbBibAjgLf2FQRSRa8-jnXO65Jtyf"))
my_var = os.environ.get("MY_VAR")
def is_w3_connected():
    return my_var

