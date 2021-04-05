/**
* file LibChameleonHash.sol
* author 某某某
* time 2021-4-5
* desc the defination of LibChameleonHash contract
*
* SPDX-License-Identifier: MIT
*
*/

pragma solidity >=0.5.16;

/*  几个注意事项：
 *  0. 代码能过编译就行，不需要在warning上面浪费时间
 *  1. 不要在合约上存东西，一些跨越函数的量比如大质数或者策略串之类的直接写死在代码里面
 *  2. 框架的参数不合理自己看着随便改
 *  3. 尽量使用ABI V2编码，这样可以实现跨合约传参时支持结构体（G1或G2点）和数组，
 *     但是如果出现了奇怪的bug就算了，默认使用ABI V1一般没有什么问题
 */

library LibChameleonHash {
    
    using LibChameleonHash for *;

    function setup() private {

    }

    function keygen() private {
        
    }

    function hash(string memory m, uint r) private returns (uint) {
        return 0;
    }

    function verify(string memory m, uint r, uint ch) private returns (bool) {
        return true;
    }

    function adapt(string memory m_old, string memory m_new, uint r) private {
        
    }
}