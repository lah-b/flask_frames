import os
from web3 import Web3

alchemy_rpc = os.environ.get("ALCHEMY_BASE_RPC")
def is_w3_connected():
    w3 = Web3(Web3.HTTPProvider(alchemy_rpc))
    return w3.isConnected()


