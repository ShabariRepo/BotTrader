import pandas as pd
from strategies import strategy_diagonal, strategy_sr, strategy_schoolrun

def load_mock_data(symbol):
    return pd.read_csv(f"data/{symbol}_mock.csv", parse_dates=["timestamp"])

def test_all_strategies():
    for symbol, strategy in [
        ("NQ", strategy_diagonal),
        ("SPY", strategy_sr),
        ("US30", strategy_schoolrun),
    ]:
        df = load_mock_data(symbol)
        df.rename(columns=str.lower, inplace=True)
        result = strategy.generate_signal(df)
        print(f"Strategy {strategy.__name__} on {symbol} returned: {result}")

if __name__ == "__main__":
    test_all_strategies()
