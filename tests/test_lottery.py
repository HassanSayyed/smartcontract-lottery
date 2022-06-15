import web3
from brownie import Lottery, accounts, config, network
from web3 import Web3

# current eth price is 1068$
# 0.046
# ~4600000000000000000

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"] ,{"from":account})
    # lottery.getEntranceFee() > Web3.toWei(0.044, "ether")
    # lottery.getEntranceFee() > Web3.toWei(0.048, "ether")
