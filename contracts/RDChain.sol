// SPDX-License-Identifier: MIT
pragma solidity >=0.5.16;

import "./LibChameleonHash.sol";

contract RDChain {

    using LibChameleonHash for *;

    uint private maxNo;
    mapping (uint => uint256) private hashList;
    mapping (uint => string) private msgList;
    mapping (uint => uint256) private rList;

    function helloworld() public pure returns(string memory) {
        return "hello world!";
    }

    function chainInit() public {
        maxNo = 0;
        msgList[0] = "redactable blockchain genesis block";
        hashList[0] = 0x0;
        rList[0] = 0x0;
    }

    function extendChain(string memory m) public pure returns (bool) {
        
        return true;
    }

    function redactBlock(uint blockNo, string memory m) public pure returns (bool) {
        return true;
    }

    function delBlock(uint blockNo) public pure returns (bool) {
        return redactBlock(blockNo, "");
    }

    function getBlock(uint blockNo) public view returns (string memory) {
        return msgList[blockNo];
    }

//   function insertBlock(uint blockNo, string memory m) public returns (bool) {
//     return true;
//   }

}
