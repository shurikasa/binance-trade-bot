#!/bin/bash

bridge_filename="bridge_list.txt"
while read -r line; do
    bridge="$line"
    coin_filename="coin_list.txt"
    while read -r line; do
        coin="$line"
        interval_filename="interval_list.txt"
        while read -r line; do
            interval="$line"
            eval "python backtest.py ${interval} ${coin} ${bridge} 2>&1| tee run_logs/${coin}${bridge}_${interval}m_0426_0714.log"
        done < "$interval_filename"
    done < "$coin_filename"
done < "$bridge_filename"
