from ib_insync import IB, Forex, Index, util
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_ibkr_candles(symbol="NQ", duration="1 D", barSize="15 mins"):
    ib = IB()
    ib.connect(os.getenv("IB_HOST"), int(os.getenv("IB_PORT")), clientId=int(os.getenv("IB_CLIENT_ID")))

    contract = Index(symbol, 'CME', 'USD') if symbol != "SPY" else Forex(symbol + "USD")
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr=duration,
        barSizeSetting=barSize,
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1
    )
    df = util.df(bars)
    ib.disconnect()
    return df
