import os
from brownie import *
from web3 import Web3
# function to deploy contract
def deploy_fallout(owr):
    # deploy contract
    sc = Fallout.deploy({'from':owr})
    return sc

def get_ownership(sc):
    sc.Fal1out({'from':accounts[2]})
    return sc.owner()

def main():
    # deployer and first owner
    owner = accounts[0]
    # deploy contract
    contract = deploy_fallout(owner)
    
    new_owner=get_ownership(contract)

    print("user 2 owner: ", new_owner == accounts[2])