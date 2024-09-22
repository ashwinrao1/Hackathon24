import random
import pygame
import sys

from Bank import changeSavings
from Bank import getSavingsBalance

transactions=[]
nos_of_medium_shares_available=200
nos_of_high_shares_available=120
nos_of_low_shares_available=350
nos_of_low_shares_owned= 0
nos_of_medium_shares_owned= 0
nos_of_high_shares_owned= 0

def low_risk_investment(current_price):
    risk_factor= random.uniform(.95,1.05)
    # multiply risk factor by current price and update current price
    current_price*= risk_factor
    return current_price

def medium_risk_investment(current_price):
    risk_factor= random.uniform(.85,1.15)
    # multiply risk factor by current price and update current price
    current_price*= risk_factor 
    return current_price

def high_risk_investment(current_price):
    risk_factor= random.uniform(.75,1.25)
    # multiply risk factor by current price and update current price
    current_price*= risk_factor
    return current_price

def calculate_money(current_price,nos_of_shares):
    return current_price*nos_of_shares

def purchase_shares(current_price,nos_of_shares_to_purchase):
    amount=calculate_money(current_price,nos_of_shares_to_purchase)
    if amount<=getSavingsBalance():
        changeSavings(-amount,"Investment")
        amount_to_purchase= -1*amount
        transactions.append(amount_to_purchase)
    else:
        print("Insufficient Funds!")

def sell_shares(current_price,nos_of_shares_to_sell):
    amount=calculate_money(current_price,nos_of_shares_to_sell)
    changeSavings(+amount,"Investment")
    amount_to_sell= amount
    transactions.append(amount_to_sell)


def calculate_net_profit(current_price,nos_of_shares):
    net_transactions=0
    for transaction in transactions:
        net_transactions+=transaction
    net_transactions*=-1
    net_profit=(current_price*nos_of_shares)- net_transactions
    return net_profit

"""print(low_risk_investment(60))
print(medium_risk_investment(60))
print(high_risk_investment(60))
print(purchase_shares(1400,58,20,nos_of_low_shares_available))
print(sell_shares(200,61,20,nos_of_medium_shares_available))
print(transactions)
print(calculate_net_profit(60,15))"""