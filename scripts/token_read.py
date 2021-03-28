#!/usr/bin/python3

from brownie import Token, accounts

# user_account = accounts.load('xxx_shared_1')
user_account = accounts.load('xxx_shared_mainnet')

def main():
    
    xxx = Token.at('0x4a6F550f6350fdD4a114b63557d13cDa2ad94643') 
    # print('%s balance: %.4f' % (token_name))
    
    smoke_test(xxx)

    
def smoke_test(token):
    token_name = token.symbol()
    decimals = token.decimals()
    print((token_name))
    print((decimals))
    print((token.balanceOf(user_account) / 10**decimals))
    # print('%s balance: %.4f' % (token_name, token.balanceOf(user_account) / 10**decimals))