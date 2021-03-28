#!/usr/bin/python3

from brownie import Token, accounts

#etherscan api
#Q9JWR2ZC58AGT4MTM7CEFI8UD8IH3VQ2WS

def main():
    # user_account = accounts.load('shared_1')
    user_account = accounts.load('shared_mainnet')
    
    Token.deploy("XXX Token", "XXX", 18, 1e26, {'from': user_account}, publish_source=True)
