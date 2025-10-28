from ib_insync import IB, Stock, MarketOrder
import os
from dotenv import load_dotenv

load_dotenv()

def connect_ibkr():
    ib = IB()
    ib.connect(os.getenv("IB_HOST"), int(os.getenv("IB_PORT")), clientId=int(os.getenv("IB_CLIENT_ID")))
    return ib

def place_trade(ib, symbol, action="BUY", qty=1):
    contract = Stock(symbol, 'SMART', 'USD')
    ib.qualifyContracts(contract)
    order = MarketOrder(action, qty)
    trade = ib.placeOrder(contract, order)
    ib.sleep(2)
    return trade.orderStatus.avgFillPrice or 0.0
