import numpy as np
import pandas as pd


# data = pd.read_excel()


def ya(x):
    return 640.9 * pow(x, 3) - 258.6 * pow(x, 2) + 37.97 * x - 1.121


def yb(x):
    return 552.8 * pow(x, 3) - 225.1 * pow(x, 2) + 33.99 * x - 1.017


def yc(x):
    return 504.7 * pow(x, 3) - 207.4 * pow(x, 2) + 32.16 * x - 0.9735


max_wa = 0.0
max_xa = 0.0

max_xb = 0.0
max_wb = 0.0

max_xc = 0.0
max_wc = 0.0

for i in range(0, 10000):
    wa = (1-ya(i/10000))*i/10000
    if wa > max_wa:
        max_wa = wa
        max_xa = i / 10000
    wb = (1 - yb(i / 10000)) * i / 10000
    if wb > max_wb:
        max_wb = wb
        max_xb = i / 10000
    wc = (1 - yc(i / 10000)) * i / 10000
    if wc > max_wc:
        max_wc = wc
        max_xc = i / 10000

print(max_xa)
print(max_wa)
print(max_xb)
print(max_wb)
print(max_xc)
print(max_wc)
