// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Fallback {
    // mapping to keep track of user and correspondent amount
    mapping(address => uint256) public contributions;
    // OWNER variable of the contract
    address public owner;

    constructor() {
        owner = msg.sender; // First owner is deployer of contract
        contributions[msg.sender] = 20 * (1 ether); 
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "caller is not the owner");
        _;
    }

    // Function to contribute
    function contribute() public payable {
        require(msg.value < 0.001 ether); // fee to contribute
        contributions[msg.sender] += msg.value; // update contribution of user
        // CHANGE OF OWNERSHIP //
        if (contributions[msg.sender] > contributions[owner]) {
            owner = msg.sender; // New owner will be the maximum contributor
        }
    }

    function getContribution() public view returns (uint256) {
        return contributions[msg.sender];
    }

    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    // send ether to contract and be owner
    receive() external payable {
        require(msg.value > 0 && contributions[msg.sender] > 0);
        // CHANGE OF OWNERSHIP //
        owner = msg.sender;
    }
}
