from web3 import Web3, Account
# from solc import compile_files
import json
import os
import pickle
import base64
import struct
from time import time
import chainUtil as chain


msgs = [
    "{from: 0x0001, to:0x0002, amount:1000, extraData:first transact}",
    "{from: 0x0003, to:0x0004, amount:2000, extraData:second transact}",
    "{from: 0x0001, to:0x0002, amount:3000, extraData:modify first transact}",
    "{from: 0x0005, to:0x0006, amount:4000, extraData:third transact}",
    "{from: 0x0005, to:0x0007, amount:4000, extraData:modify third transact}",
]


def main():

    # offline part init

    chain.hashInit()

    # connect to blockchain and deploy contract

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting to block chain')

    print("connected to blockchain.\n")

    contract_instance = chain.DeployContract()

    print("contract deployed.\n")

    chain.addBlock(msgs[0])

    chain.addBlock(msgs[1])

    chain.modifyBlock(1, msgs[2])

    chain.addBlock(msgs[3])

    chain.modifyBlock(3, msgs[4])


if __name__ == "__main__":
    main()
