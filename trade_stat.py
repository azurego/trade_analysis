#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd
from pandas import DataFrame

UNIT_PER_LOT = { \
    "rb": 10, "ru": 10, "hc": 10, "cu": 5, "zn": 5, "al": 5, "bu": 10,   \
    "i": 100, "j": 100, "y": 10, "p": 10, "m": 10, "c": 10, "a": 10, "cs": 10,   \
    "jm": 100, "l": 5, "pp":5, \
    "TA": 5, "SR": 5, "CF": 5, "RM": 10, "FG": 10, "OI": 10,   \
    "IF": 300, "IC": 200, "IH": 300 \
    }


def contract_to_commodity(contract):

    return re.sub(r'[\d]+', '', contract)


def stat_contract(contract, data):

    which = data['contract'] == contract
    df_contract = data[which]
    df_contract_long = df_contract[ df_contract['direction'] == 0 ]
    df_contract_short = df_contract[ df_contract['direction'] != 0 ]

    contract_long_money = df_contract_long['price'] * df_contract_long['volume'] \
                            * UNIT_PER_LOT[contract_to_commodity(contract)]
    contract_short_money = df_contract_short['price'] * df_contract_short['volume'] \
                            * UNIT_PER_LOT[contract_to_commodity(contract)]

    win_money = contract_long_money.sum() - contract_short_money.sum()
    print contract, "win money:", win_money


if __name__ == "__main__":

    df = pd.read_csv("trade_sample.csv")
    
    contracts = df['contract'].unique()
    contracts.sort()

    for item in contracts:
        stat_contract(item, df)
    
#    stat_contract("rb1705", df)
#    stat_contract("ru1705", df)

