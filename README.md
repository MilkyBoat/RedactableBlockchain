# Redactable Block Chain

> implement of paper ` `

---

## requirement

#### tool application or framework
* truffle ~=5.3.0
* ganache-cli ~=6.12.2
* python3 >= 3.5

#### python lib
* web3 ~=5.17.0

The version of requirements does not need to be strictly complied with. Follow the instructions following generally does not cause compatibility problems

`for linux user`
```bash
# If you are in some certain areas, remember to switch sources of `apt-get`/`npm`/`pip3` before installation
sudo apt-get install nodejs
sudo apt-get install npm
sudo npm install -g truffle
sudo npm install -g ganache-cli
pip3 install web3
```

`for windows user`

1. download and run [nodejs release for windows](https://nodejs.org/dist/v14.16.1/node-v14.16.1-x64.msi)

2. download and install python3 with [anaconda](https://www.anaconda.com/products/individual#Downloads) or [python3](https://www.python.org/downloads/)

    // 2.5 If you are in some certain areas, remember to switch sources of `pip` or `npm` before installation

3. open a powershell tab with administrator privileges
    ```bash
    npm install -g truffle
    npm install -g ganache-cli
    pip install web3
    ```

---

## how to run

### 0. Clone me
```bash
git clone https://github.com/MilkyBoat/RedactableBlockchain.git
cd RedactableBlockchain
```

### 1. Start up a blockchain

```bash
ganache-cli -g 1 -l 9007199254740991 --db ./RDBlockchain -s 1234 -a 2
```

### 2. Compile contracts

```bash
# open a new terminal tab 
truffle compile
```

### 3. Run apps

```bash
cd app
# make sure ganache-cli has showen "Listening on 127.0.0.1:8545"
python3 RDChain.py
```

### 4. Expected output

1. terminal 1 (`ganache-cli`)
```
Ganache CLI v6.12.2 (ganache-core: 2.13.2)

Available Accounts
==================
(0) 0x433220a86126eFe2b8C98a723E73eBAd2D0CbaDc (100 ETH)
(1) 0xAa90c43123ACEc193A35D33db5D71011B019779D (100 ETH)

Private Keys
==================
(0) 0x9e72e5257645bebc6e3423696be498c6973cc23cee4aaad507d04331d51fcef6
(1) 0xc9f2b0f3e426d1c1762969646514c6867a344280a426a0c19a8e1ceff165c652

HD Wallet
==================
Mnemonic:      fame elevator saddle renew match guilt seat duck seven buyer true smoke
Base HD Path:  m/44'/60'/0'/0/{account_index}

Gas Price
==================
1

Gas Limit
==================
9007199254740991

Call Gas Limit
==================
9007199254740991

Listening on 127.0.0.1:8545
web3_clientVersion
web3_clientVersion
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x0ee07c2213bc468d302037f3cf50f820b98e5b9576a9331fb65866b3cfe56359
  Contract created: 0xefbf81372abc3723463746a89ceb42080563684c
  Gas usage: 230054
  Block Number: 1
  Block Time: Fri Apr 09 2021 00:06:04 GMT+0800 (中国标准时间)

eth_getTransactionReceipt
web3_clientVersion
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x1766f6b9c11696c670e31b69779acca4ffe65cfb16ebb737190805ad6fe93e6e
  Gas usage: 86769
  Block Number: 2
  Block Time: Fri Apr 09 2021 00:06:05 GMT+0800 (中国标准时间)

eth_getTransactionReceipt
web3_clientVersion
eth_accounts
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x936deaee8d24511074696e7a0ec2f90b4b0bd6a0d30f22c8a90569dfd5e24a16
  Gas usage: 53768
  Block Number: 3
  Block Time: Fri Apr 09 2021 00:06:05 GMT+0800 (中国标准时间)

web3_clientVersion
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0x4dd1c5fbd327c9bc0ac8b9f9b0b02da8663093ae4ebfbae457e23cd5ac3f2a36
  Gas usage: 71769
  Block Number: 4
  Block Time: Fri Apr 09 2021 00:06:05 GMT+0800 (中国标准时间)

eth_getTransactionReceipt
web3_clientVersion
eth_call
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xe1b2c547ad9f596d803cc1596c2c664c3d2063fa2967f9bcbfbe3835ab03013a
  Gas usage: 28456
  Block Number: 5
  Block Time: Fri Apr 09 2021 00:06:05 GMT+0800 (中国标准时间)

eth_getTransactionReceipt
web3_clientVersion
eth_accounts
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xbddf0fcb77fa585da0af9bc72669cdce32e08122ce03d598f3be119082546014
  Gas usage: 348680
  Block Number: 6
  Block Time: Fri Apr 09 2021 00:06:06 GMT+0800 (中国标准时间)

web3_clientVersion
eth_accounts
eth_accounts
eth_estimateGas
eth_blockNumber
eth_getBlockByNumber
eth_sendTransaction

  Transaction: 0xc5d8186fb9b8caab5d38a80b5d41789467031529e0cf028158f93f8c60076819
  Gas usage: 56008
  Block Number: 7
  Block Time: Fri Apr 09 2021 00:06:06 GMT+0800 (中国标准时间)
```
2. terminal 2 (`truffle && python`)
```
connected to blockchain.

contract deployed.

test 1:
transact recorded to chain
  msg length : 1024
  block no : 1
  chameleon hash : 16071974862613351640328311756013783866904970418285876715407049007615
  random number : 600430487660208764927304999270793887745616306529840116892573253
++time used : 0.3028855323791504 s


transact recorded to chain
  msg length : 2048
++time used : 0.19356727600097656 s


test 2:
dataBlockNum: 10
transact recorded to chain
  msg length : 10240
  block no : 2
  chameleon hash : 7565707993708199954549580095410611780727352701128329215539746688753
  random number : 1576399222253064597341520896640782163787722955889969405346769380
++time used : 0.26924967765808105 s

transact modified
  new msg length : 10240
  block no : 2
  new chameleon hash : 7565707993708199954549580095410611780727352701128329215539746688753
  new random number : 989286933877900743108947364564718049516316510260880715882468091
++time used : 0.26438021659851074 s


test 3:
dataBlockNum: 10
transact recorded to chain
  msg length : 20480
++time used : 0.27454543113708496 s

transact recorded to chain
  msg length : 2188
++time used : 0.14151811599731445 s
```

