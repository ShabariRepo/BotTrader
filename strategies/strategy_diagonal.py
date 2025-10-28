from indicators import ema, slope, find_trendline_points
import pandas as pd

def generate_signal(candles: pd.DataFrame) -> dict:
    if len(candles) < 60:
        return {"action": "HOLD"}

    candles['ema50'] = ema(candles['close'], 50)
    candles['ema_slope'] = slope(candles['ema50'])

    latest = candles.iloc[-1]
    trendline_pts = find_trendline_points(candles, side="long")

    if latest['close'] > latest['ema50'] and latest['ema_slope'] > 0 and trendline_pts:
        i, level = trendline_pts[-1]
        if abs(latest['close'] - level) < 1.0:
            return {
                "action": "BUY",
                "symbol": "NQ",
                "qty": 1,
                "strategy_name": "strategy_diagonal",
                "note": "Diagonal trendline retest near mechanical rejection"
            }

    return {"action": "HOLD"}
