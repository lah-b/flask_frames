import os
from web3 import Web3
from .abi import sep_abi


CONTRACT_ABI = sep_abi()
alc_base_sep_rpc = os.environ.get("ALCHEMY_BASE_SEP_RPC")


def get_tx_data(acct_address):
    try:
        w3 = Web3(Web3.HTTPProvider(alc_base_sep_rpc))
        my_contract = w3.eth.contract(
            address="0x40eA87a0DffaD828778EB248156DF01A358f541b", abi=CONTRACT_ABI
        )
        build_tx = my_contract.functions.mintPill().build_transaction(
            {"from": acct_address}
        )
        tx_data = build_tx["data"]
        return tx_data

    except Exception as e:
        print("Connection failed:", e)
        return 0
