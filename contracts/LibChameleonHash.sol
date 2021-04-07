/**
* file LibChameleonHash.sol
* author xu yunkai
* time 2021-4-5
* desc the defination of LibChameleonHash contract
*
* SPDX-License-Identifier: MIT
*
*/

pragma solidity >=0.5.16;

import "./utillib/Curve.sol";

library LibChameleonHash {
    
    using LibChameleonHash for *;

    function setup() private {

    }

    function keygen() private {
        
    }

    function hash(string memory m, uint256 r) private pure returns (uint256) {

        // hash m to int
        bytes32 mHashb = sha256(bytes(m));
        uint256 mHash = 0;
        for(uint8 i = 0; i < 32; i++) {
            mHash = mHash + uint256(uint8(mHashb[i]))*(2**(8*(31-i)));
        }
        
        uint256 ch;

        return 0;
    }

    function verify(string memory m, uint256 r, uint256 ch) private returns (bool) {
        return hash(m, r) == ch;
    }

    function forge(string memory m_old, string memory m_new, uint256 r) private {
        
    }
}