import datetime

def generate_signal(candles):
    now = datetime.datetime.utcnow()
    if now.hour == 14 and now.minute < 15:
        return {"action": "BUY", "symbol": "US30", "qty": 1, "strategy_name": "strategy_schoolrun", "note": "Morning volatility window"}
    return {"action": "HOLD"}
