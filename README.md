# steembank.howmuch

스팀뱅크의 금액 계산 자동화 프로그램

### Installation

```bash
git clone https://github.com/taeminlee/steembank.howmuch
cd steembank.howmuch
pip install requests prettytable babel
python howmuch.py
```

### Running Example

```bash
모드 선택, 1 : KRW->SBD, 2 : SBD -> KRW
1
금액 입력
50000
2017-09-01 18:52:15
빗썸 BTC 가격 조회중...
비트렉스 SBD 가격 조회중...
+----------------+-----------+
|      항목      |    가격   |
+----------------+-----------+
|    BTC(KRW)    | 5,290,000 |
|    SBD(BTC)    | 0.0002191 |
|    SBD(KRW)    |   1,159   |
| 수신 금액(KRW) |   50,000  |
| 환산 금액(SBD) |  43.1392  |
|  수수료 (SBD)  |    1.0    |
| 최종 금액(SBD) |  42.1392  |
+----------------+-----------+
모드 선택, 1 : KRW->SBD, 2 : SBD -> KRW
2
금액 입력
50
2017-09-01 18:52:21
빗썸 BTC 가격 조회중...
비트렉스 SBD 가격 조회중...
+----------------+-----------+
|      항목      |    가격   |
+----------------+-----------+
|    BTC(KRW)    | 5,290,000 |
|    SBD(BTC)    | 0.0002191 |
|    SBD(KRW)    |   1,159   |
| 수신 금액(SBD) |     50    |
| 환산 금액(KRW) |   57,952  |
|  수수료 (KRW)  |   1,159   |
| 최종 금액(KRW) |   56,793  |
+----------------+-----------+
```