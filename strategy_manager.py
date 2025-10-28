import pandas as pd
from strategies import strategy_diagonal, strategy_sr, strategy_schoolrun
from db_utils import log_trade
from ibkr_utils import connect_ibkr, place_trade

def run_strategies(candles: pd.DataFrame, live_run=False):
    ib = connect_ibkr()
    strategies = [
        strategy_diagonal.generate_signal,
        strategy_sr.generate_signal,
        strategy_schoolrun.generate_signal
    ]
    for strat_fn in strategies:
        strat = strat_fn(candles)
        if strat["action"] in ("BUY", "SELL"):
            price = place_trade(ib, strat["symbol"], strat["action"], strat["qty"])
            if live_run:
                log_trade(strat["symbol"], strat["strategy_name"], strat["action"], strat["qty"], price, strat["note"])
            print(f"Executed {strat['strategy_name']}: {strat['action']} {strat['qty']} {strat['symbol']} at {price}")
    ib.disconnect()
