// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vault {
  bool public locked;
  bytes32 private password;

  constructor(bytes32 _password) {
    locked = true;
    password = _password;
  }

  function unlock(bytes32 _password) public {
    if (password == _password) {
      locked = false;
    }
  }
}

contract Cracker{
    Vault public vault;
    bool public locked;
    bytes32 private password;
    
    constructor(address _addressvault) {
      vault = Vault(_addressvault);
      locked = true;
      password = bytes32('hacked');
    }

    function crack() public{
      vault.unlock(password);
    }
}