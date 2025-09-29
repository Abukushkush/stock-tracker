import random

def scan_breakouts():
    tickers = ["AAPL", "TSLA", "NVDA", "AMD", "MSFT"]
    results = [{"ticker": t, "breakout": bool(random.getrandbits(1))} for t in tickers]
    return [r for r in results if r["breakout"]]
