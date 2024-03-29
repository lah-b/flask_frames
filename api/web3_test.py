import os
from web3 import Web3
from .abi import abi


CONTRACT_ABI = abi()
alchemy_rpc = os.environ.get("ALCHEMY_BASE_RPC")


def is_w3_connected():
    try:
        # w3 = Web3(Web3.HTTPProvider(alchemy_rpc))
        # data = w3.eth.get_block('latest')
        # my_contract = w3.eth.contract(
        #     address="0xD09d72031Ce8212efD8928F1A3814E7F8da0fDfD",
        #     abi=CONTRACT_ABI
        # )
        # mint_price = my_contract.functions.mintPrice().call()
        # return mint_price
        return 69
    except Exception as e:
        print("Connection failed:", e)
        return 0
