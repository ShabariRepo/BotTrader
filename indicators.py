import pandas as pd

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def slope(series, period=5):
    return (series - series.shift(period)) / period

def find_trendline_points(candles, side="long"):
    points = []
    for i in range(2, len(candles) - 2):
        if side == "long":
            if candles['low'][i] < candles['low'][i-1] and candles['low'][i] < candles['low'][i+1]:
                points.append((i, candles['low'][i]))
        else:
            if candles['high'][i] > candles['high'][i-1] and candles['high'][i] > candles['high'][i+1]:
                points.append((i, candles['high'][i]))
    return points[-3:] if len(points) >= 3 else []
