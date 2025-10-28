def generate_signal(candles):
    if len(candles) < 30:
        return {"action": "HOLD"}

    support = min(candles['low'][-20:])
    resistance = max(candles['high'][-20:])
    last_close = candles['close'].iloc[-1]

    if abs(last_close - support) < 0.5:
        return {"action": "BUY", "symbol": "SPY", "qty": 1, "strategy_name": "strategy_sr", "note": "Near support"}
    elif abs(last_close - resistance) < 0.5:
        return {"action": "SELL", "symbol": "SPY", "qty": 1, "strategy_name": "strategy_sr", "note": "Near resistance"}

    return {"action": "HOLD"}
