from web3 import Web3
import os

alchemy_base_rpc = os.environ.get("ALCHEMY_BASE_RPC")
w3 = Web3(Web3.HTTPProvider(alchemy_base_rpc))


def is_w3_connected():
    return w3.is_connected()


if __name__ == "__main__":
    print(is_w3_connected())
