from web3 import Web3, Account
import json
import binascii
import random
from time import time
import ChameleonHash as ch

chainData = {}
contract_instance = None
SK = 0
PK = 0

def hashInit():
    global SK, PK
    SK = ch.getSecretKey()
    PK = ch.getPublicKey(SK)


def DeployContract(contract_path='../build/contracts/RDChain.json'):

    global contract_instance

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
	    raise Exception('error in connecting')

    with open(contract_path, 'r', encoding='utf-8') as contract_json_file:

        if contract_json_file is None:
            raise Exception("complied contract not found at " + contract_path)

        contract_json = json.load(contract_json_file)
        contract = w3.eth.contract(abi=contract_json['abi'], bytecode=contract_json['bytecode'])
        tx_hash = contract.constructor().transact({'from': w3.eth.accounts[0]})
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        contractAddress = tx_receipt.contractAddress
        contract_instance = w3.eth.contract(address=contractAddress, abi=contract_json['abi'])

        return contract_instance


def addSimpleBlock(msg: str):
    
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting')
    
    t0 = time()

    msg = binascii.hexlify(bytes(msg, encoding="utf8"))

    w3.eth.sendTransaction({"from": w3.eth.accounts[0], "to": w3.eth.accounts[1], "data": msg})

    # print("%.6f-%d" % ((time()-t0), w3.eth.get_block('latest').gasUsed), end=' ')
    print("transact recorded to chain")
    print("  msg length :", len(msg))
    print("++time used :", time()-t0, "s")
    print()


def addBlock(msg: str) -> int:

    global chainData

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting')

    t0 = time()

    r = random.randint(1, ch.q)
    chash = ch.ChameleonHash(PK, ch.g, msg, r)

    tx_hash = contract_instance.functions.extendChain(chash, r).transact({'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    tx_res = contract_instance.events.entendResult().processReceipt(tx_receipt)
    blockNo = tx_res[0]['args']['blockNo']

    chainData[blockNo] = msg

    # print("%.6f-%d" % ((time()-t0), w3.eth.get_block('latest').gasUsed), end=' ')
    print("transact recorded to chain")
    print("  msg length :", len(msg))
    print("  block no :", blockNo)
    print("  chameleon hash :", chash)
    print("  random number :", r)
    print("++time used :", time()-t0, "s")
    print()

    return blockNo


def modifyBlock(blockNo: int, newMsg: str):
    
    global chainData

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting')

    _, r = contract_instance.functions.getBlock(blockNo).call()
     
    t0 = time()
       
    r_ = ch.Forge(SK, chainData[blockNo], r, newMsg)
    newChash = ch.ChameleonHash(PK, ch.g, newMsg, r_)

    tx_hash = contract_instance.functions.redactBlock(blockNo, newChash, r_).transact({'from': w3.eth.accounts[0]})
    w3.eth.waitForTransactionReceipt(tx_hash)

    chainData[blockNo] = newMsg

    # print("%.6f-%d" % ((time()-t0), w3.eth.get_block('latest').gasUsed), end=' ')
    print("transact modified")
    print("  new msg length :", len(newMsg))
    print("  block no :", blockNo)
    print("  new chameleon hash :", newChash)
    print("  new random number :", r_)
    print("++time used :", time()-t0, "s")
    print()


def test(contract_instance):
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
	    raise Exception('error in connecting')

    contract_instance.functions.helloworld().transact({'from': w3.eth.accounts[0]})


if __name__ == "__main__":

    contract_instance = DeployContract()
    print(contract_instance)
    test(contract_instance)
    