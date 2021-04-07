// SPDX-License-Identifier: MIT

pragma solidity >=0.5.16;

contract RDChain {

    uint private maxNo;
    mapping (uint => uint256) private hashList;
    mapping (uint => uint256) private rList;

    event entendResult(uint blockNo);

    function helloworld() public pure returns(string memory) {
        return "hello world!";
    }

    constructor() public {
        maxNo = 0;
        hashList[0] = 0x0;
        rList[0] = 0x0;
    }

    function getBlock(uint blockNo) public view returns (uint ch, uint r) {
        return (hashList[blockNo], rList[blockNo]);
    }

    function getMaxNo() public view returns (uint) {
        return maxNo;
    }

    function extendChain(uint256 ch, uint256 r) public {
        maxNo++;
        hashList[maxNo] = ch;
        rList[maxNo] = r;
        emit entendResult(maxNo);
    }

    function redactBlock(uint blockNo, uint256 ch, uint256 r) public {
        hashList[blockNo] = ch;
        rList[blockNo] = r;
    }

    // function delBlock(uint blockNo) public returns (bool) {
    //     return redactBlock(blockNo, 0x0, 0x0);
    // }

    // function insertBlock(uint blockNo, string memory m) public returns (bool) {
    // return true;
    // }

}
