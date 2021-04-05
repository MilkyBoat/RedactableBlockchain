#!/bin/bash

geth --identity "rdethereum" \
     --rpc --rpcaddr "127.0.0.1" \
     --port 30304 \
     --rpcport "7545" \
     --rpccorsdomain "*" \
     --datadir ../RDBlockchain \
     --rpcapi "db,eth,net,web3,admin,personal" \
     --networkid 2333 \
     console \
     --allow-insecure-unlock
