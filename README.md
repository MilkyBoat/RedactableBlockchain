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
ganache-cli -l 9007199254740991 --db ./RDBlockchain -s 1234
```

### 2. Compile contracts

```bash
# open a new terminal tab 
truffle compile
```

### 3. Run apps

```bash
cd app
python3 RDChain.py
```

### 4. Expected output

1. terminal 1 (`ganache-cli`)
```

```
2. terminal 2 (`truffle && python`)
```

```

