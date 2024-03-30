import os
from web3 import Web3
from .abi import abi


CONTRACT_ABI = abi()
qn_rpc = os.environ.get("ALCHEMY_BASE_RPC")

my_acct = "0x9f3268BaA5a163Ce4fa3eE49F7AA7DAf2b97Fc8a"
acct_2 = "0x585a6b5E1fA425eAEd742adb23607C6b8342949F"


def get_tx_data(acct_address):
    try:
        w3 = Web3(Web3.HTTPProvider(qn_rpc))
        my_contract = w3.eth.contract(
            address="0xD09d72031Ce8212efD8928F1A3814E7F8da0fDfD", abi=CONTRACT_ABI
        )
        build_tx = my_contract.functions.safeTransferFrom(
            acct_address, my_acct, 3
        ).build_transaction({"from": acct_address})
        tx_data = build_tx["data"]
        return tx_data

    except Exception as e:
        print("Connection failed:", e)
        return 0
