// SPDX-License-Identifier: MIT
pragma solidity >=0.5.16 <0.9.0;

contract RDChain {

    mapping (address => uint) private saltList;

    function helloworld() public pure returns(string memory) {
        return "hello world!";
    }

    function extendChain(string memory m) public returns (bool) {
        return true;
    }

    function redactBlock(address blockAddr, string memory m) public returns (bool) {
        return true;
    }

    function delBlock(address blockAddr) public returns (bool) {
        return true;
    }

//   function insertBlock(uint blockNo, string memory m) public returns (bool) {
//     return true;
//   }

}
