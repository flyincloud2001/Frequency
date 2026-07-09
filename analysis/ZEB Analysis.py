import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

START = '2024-01-01'
END = '2026-06-30'
SYMBOL = 'ZEB.TO'

raw = yf.download(SYMBOL, start=START, end=END, auto_adjust=True)
data = raw[['Close', 'High']].copy()
data['change'] = data['High']/data['Close'].shift(1)
data.dropna(inplace=True)

percentages = [1.005, 1.01, 1.015, 1.02, 1.025, 1.03]
perfs = []
perfs = []
sizes = []
sizes = []

higher_than_1_percent = data[data['change'] >= 1.01].index
print(len(higher_than_1_percent))

for i in percentages:
    size = ((data['change'] >= i) & (data['change'] < i+0.005)).sum()
    sizes.append(size)
    perfs.append(f'{i:.2%} =< % < {(i+0.005):.2%}: {size} days')

for line in perfs:
    print(line)



fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(data['change'], label='price change in %', linewidth=0.5)
for x in higher_than_1_percent:
    ax.axvline(x, color='r', alpha=0.5, linewidth=1, linestyle='--')
ax.set_xlabel('dates')
ax.set_ylabel('changes')
ax.set_title('prices changes in %')
ax.grid()
plt.tight_layout()
plt.savefig("prices_changes_in_%", dpi=150)
plt.show()


