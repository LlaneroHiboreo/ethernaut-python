import os
from brownie import *
from web3 import Web3

# function to deploy contract
def deploy_flip(owr):
    # deploy contract flip
    scf = CoinFlip.deploy({'from':owr})
    sch = HackCoinFlips.deploy(scf.address, {'from':owr})
    return scf,sch

def make_guess(sc_flip, sc_hack):
    for ges in range(0,10):
        sc_hack.gess()
        print(sc_flip.consecutiveWins())

def main():
    # deployer and first owner
    owner = accounts[0]
    # deploy contract
    c_f, c_h = deploy_flip(owner)
    # make guess
    make_guess(c_f,c_h)
