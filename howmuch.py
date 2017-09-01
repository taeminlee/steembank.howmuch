# import python libs
import sys
import re
import time
import json
from datetime import datetime
from collections import OrderedDict
# import additional libs
import requests as req
from prettytable import PrettyTable
# import pyTicker libs
import exchange
import util
from babel.numbers import format_decimal

currencies = ["SBD"]
cols = ["SBD", "BTC"]

fee_SBD = 1.0

print("init howmuch.. It takes several seconds..")

def howmuch():
    try:
        print("모드 선택, 1 : KRW->SBD, 2 : SBD -> KRW")
        mode = int(input())
        print("금액 입력")
        amount = int(input())
        if mode == 1 or mode == 2 :
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("빗썸 BTC 가격 조회중...")
            bithumb_last, bithumb_KRW_last = exchange.get_bithumb_last(currencies)
            print("비트렉스 SBD 가격 조회중...")
            bittrex_last, bittrex_USDT_last = exchange.get_bittrex_last(currencies)
            sbd1 = 1 *bittrex_last['SBD'] * bithumb_KRW_last['BTC']
            t = PrettyTable(["항목", "가격"])
            t.add_row(["BTC(KRW)", util.KRW(bithumb_KRW_last['BTC'])])
            t.add_row(["SBD(BTC)", bittrex_last['SBD']])
            t.add_row(["SBD(KRW)", util.KRW(sbd1)])
            if mode == 1:
                t.add_row(["수신 금액(KRW)", util.KRW(amount)])
                conv_amount = amount / bithumb_KRW_last['BTC'] / bittrex_last['SBD']
                t.add_row(["환산 금액(SBD)", round(conv_amount, 4)])
                t.add_row(["수수료 (SBD)", round(fee_SBD, 4)])
                t.add_row(["최종 금액(SBD)", round(conv_amount - fee_SBD, 4)])
            if mode == 2:
                t.add_row(["수신 금액(SBD)", round(amount, 4)])
                conv_amount = amount * bithumb_KRW_last['BTC'] * bittrex_last['SBD']
                fee = fee_SBD *bittrex_last['SBD'] * bithumb_KRW_last['BTC']
                t.add_row(["환산 금액(KRW)", util.KRW(conv_amount)])
                t.add_row(["수수료 (KRW)", util.KRW(fee)])
                t.add_row(["최종 금액(KRW)", util.KRW(conv_amount - fee)])
            print(t)
    except Exception as e:
        #slack_bot.chat.post_message("#error", "failed with error code: {}".format(e))
        print("failed with error code: {}".format(e))

if __name__ == "__main__":
    while 1:
        howmuch()