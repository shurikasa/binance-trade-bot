from datetime import datetime
from binance_trade_bot import backtest
import sys

if __name__ == "__main__":
    interval = 1
    starting_coin = None
    bridge = None
    start_balance = 100
    if (len(sys.argv) > 1):
        interval = int(sys.argv[1])
        starting_coin = sys.argv[2]
        bridge = sys.argv[3]
        start_balance = sys.argv[4]
    print(f"Starting coin: {starting_coin}, bridge: {bridge}, interval: {interval}")
    history = []
    for manager in backtest(datetime(2021, 4, 26), datetime(2021, 7, 14), interval = interval, starting_coin = starting_coin, bridge = bridge, start_balances = {starting_coin: start_balance}):
        btc_value = manager.collate_coins("BTC")
        bridge_value = manager.collate_coins(manager.config.BRIDGE.symbol)
        history.append((btc_value, bridge_value))
        btc_diff = round((btc_value - history[0][0]) / history[0][0] * 100, 3)
        bridge_diff = round((bridge_value - history[0][1]) / history[0][1] * 100, 3)
        print("------")
        print("TIME:", manager.datetime)
        print("BALANCES:", manager.balances)
        print("BTC VALUE:", btc_value, f"({btc_diff}%)")
        print(f"{manager.config.BRIDGE.symbol} VALUE:", bridge_value, f"({bridge_diff}%)")
        print("------")
