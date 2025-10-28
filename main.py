from fetch_candles import get_ibkr_candles
from strategy_manager import run_strategies

if __name__ == "__main__":
    candles = get_ibkr_candles("NQ", duration="1 D", barSize="15 mins")
    run_strategies(candles, live_run=True)
