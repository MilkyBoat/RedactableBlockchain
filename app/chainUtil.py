from web3 import Web3, Account
import json
import ChameleonHash as ch
import random

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

    # 连接本地区块链网络
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    # 判断是否连接上
    if w3.isConnected() is False:
	    raise Exception('error in connecting')

    # 加载本地的已经编译的合约文件，将其解码后去除abi部分和bytecode，生成合约对象
    with open(contract_path, 'r', encoding='utf-8') as contract_json_file:

        if contract_json_file is None:
            raise Exception("complied contract not found at " + contract_path)

        # 发起一次交易，内容是合约的构造函数，这种交易实质上是对合约的部署，发起者是默认账户，接收者等信息均为空
        contract_json = json.load(contract_json_file)
        contract = w3.eth.contract(abi=contract_json['abi'], bytecode=contract_json['bytecode'])
        # 部署合约到区块链上
        tx_hash = contract.constructor().transact({'from': w3.eth.accounts[0]})
        # 查看回执
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        contractAddress = tx_receipt.contractAddress
        contract_instance = w3.eth.contract(address=contractAddress, abi=contract_json['abi'])
        # 返回合约对象
        return contract_instance


def addBlock(msg: str) -> int:

    global chainData

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting')

    r = random.randint(1, ch.q)
    chash = ch.ChameleonHash(PK, ch.g, msg, r)

    tx_hash = contract_instance.functions.extendChain(chash, r).transact({'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    tx_res = contract_instance.events.entendResult().processReceipt(tx_receipt)
    blockNo = tx_res[0]['args']['blockNo']

    chainData[blockNo] = msg

    print("transact recorded to chain")
    print("  msg :", msg)
    print("  block no :", blockNo)
    print("  chameleon hash :", chash)
    print("  random number :", r)
    print()

    return blockNo


def modifyBlock(blockNo: int, newMsg: str):
    
    global chainData

    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    if w3.isConnected() is False:
        raise Exception('error in connecting')

    chash, r = contract_instance.functions.getBlock(blockNo).call()
        
    r_ = ch.Forge(SK, chainData[blockNo], r, newMsg)
    newChash = ch.ChameleonHash(PK, ch.g, newMsg, r_)

    tx_hash = contract_instance.functions.redactBlock(blockNo, newChash, r_).transact({'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    chainData[blockNo] = newMsg

    print("transact modified")
    print("  new msg :", newMsg)
    print("  block no :", blockNo)
    print("  new chameleon hash :", newChash)
    print("  new random number :", r_)
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
    