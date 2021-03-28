#!/usr/bin/python3

from brownie import Token, accounts

# user_account = accounts.load('xxx_shared_1')
user_account = accounts.load('xxx_shared_mainnet')

def main():
    
    xxx = Token.at('0x4a6F550f6350fdD4a114b63557d13cDa2ad94643') 
    destination_account = "0xE1D421c7Aa33eA4676656323B9cc131ca16ab11c";
    send_amount = 123
    # print('%s balance: %.4f' % (token_name))
    
    send(xxx, destination_account, send_amount)

    
def send(token, destination_account, send_amount):
    decimals = token.decimals()

    token.transfer(destination_account, send_amount * 10**decimals, {'from': user_account})