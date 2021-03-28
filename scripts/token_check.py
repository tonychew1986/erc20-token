#!/usr/bin/python3

from brownie import Token, accounts

#etherscan api
#Q9JWR2ZC58AGT4MTM7CEFI8UD8IH3VQ2WS

def main():
    # user_account = accounts.load('xxx_shared_1')
    # user_account = accounts.load('xxx_shared_mainnet')
    
    
    token_contract = Token.at("0xe63d6B308BCe0F6193AeC6b7E6eBa005f41e36AB")  # use the address where the contract is deployed
    Token.publish_source(token_contract)