import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

START = '2010-01-01'
END = '2026-06-30'
SYMBOL = 'ZEB.TO'

raw = yf.download(SYMBOL, start=START, end=END, auto_adjust=True)
data = raw[['Close', 'High']].copy()
data['change'] = data['High']/data['Close'].shift(1)
data.dropna(inplace=True)

percentages = [1.005, 1.01, 1.015, 1.02, 1.025, 1.03]
perfs = []
sizes = []
for i in percentages:
    size = ((data['change'] >= i) & (data['change'] < i+0.005)).sum()
    sizes.append(size)
    perfs.append(f'{i:.2%} =< % < {(i+0.005):.2%}: {size} days')

for line in perfs:
    print(line)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(data['change'], label='price change in %', linewidth=0.5)
ax.set_xlabel('dates')
ax.set_ylabel('changes')
ax.set_title('prices changes in percentages')
ax.grid()
plt.tight_layout()
plt.show()


