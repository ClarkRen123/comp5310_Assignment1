import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import warnings
import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)
plt.figure(figsize=(12, 8))
plt.plot(data['Date'], data['Open'], label='Open')
plt.plot(data['Date'], data['High'], label='High')
plt.plot(data['Date'], data['Low'], label='Low')
plt.plot(data['Date'], data['Close'], label='Close')
plt.plot(data['Date'], data['Adj Close'], label='Adj Close')
plt.plot(data['Date'], data['AMD'], label='AMD')
plt.plot(data['Date'], data['ASML'], label='ASML')
plt.plot(data['Date'], data['QCOM'], label='QCOM')
plt.plot(data['Date'], data['TXN'], label='TXN')
plt.plot(data['Date'], data['INTEL'], label='INTEL')

plt.title('NVDA stock price vs other semiconductor companies from 2018-2022')
plt.xlabel('Year')
plt.ylabel('$')
plt.legend()
plt.grid(True)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')
ax1.plot(data['Date'], data['Close'], label='Close')
ax1.plot(data['Date'], data['Open'], label='Open')
ax1.plot(data['Date'], data['High'], label='High')
ax1.plot(data['Date'], data['Low'], label='Low')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('Volume')
ax2.plot(data['Date'], data['Volume'], color = 'tab:gray',label='Volume')
ax2.tick_params(axis='y')
fig.tight_layout()
plt.title('NVDA price vs volume')
fig.legend()
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel('Date')
ax1.set_ylabel('NVIDIA Close price')
ax1.plot(data['Date'], data['Close'], label='Close')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('crypto price')
ax2.plot(data['Date'], data['BTC'], color = 'tab:red',label='BTC')
ax2.plot(data['Date'], data['ETH'], color = 'tab:green',label='ETH')
ax2.tick_params(axis='y')
fig.tight_layout()
plt.title('NVDA price vs crypto currency')
fig.legend()
plt.show()


fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel('Date')
ax1.set_ylabel('NVIDIA trade volume')
ax1.plot(data['Date'], data['Volume'], label='NVDA Volume')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('crypto trade volume')
ax2.plot(data['Date'], data['BTC-Volume'], color = 'tab:red',label='BTC Volume')
ax2.plot(data['Date'], data['ETH-Volume'], color = 'tab:green',label='ETH Volume')
ax2.tick_params(axis='y')
fig.tight_layout()
plt.title('NVDA volume vs crypto currency')
fig.legend()
plt.show()



'''
NVIDIA release'] = NVR
result_df['NVIDIA median performance'] = NVP1
result_df['NVIDIA maximum performance'] = NVP2
result_df['others release'] = OTR
result_df['others median performance'] = OTP1
result_df['others maximum performance
'''
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_xlabel('Date')
ax1.set_ylabel('NVIDIA close price $')
ax1.plot(data['Date'], data['Close'], color = 'tab:cyan',label='NVDA Close price')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('benchmark data')
ax2.plot(data['Date'], data['NVIDIA median performance'], label='NVIDIA median performance')
ax2.plot(data['Date'], data['NVIDIA maximum performance'], label='NVIDIA maximum performance')
ax2.plot(data['Date'], data['others median performance'], label='others median performance')
ax2.plot(data['Date'], data['others maximum performance'], label='others maximum performance')
ax2.plot(data['Date'], data['NVIDIA release'], label='NVIDIA release')
ax2.plot(data['Date'], data['others release'], label='others release')
ax2.tick_params(axis='y')
fig.tight_layout()
plt.title('NVDA close price vs benchmark test data')
fig.legend()
plt.show()


plt.scatter(data['Close'],data['ASML'],data['AMD'],data['QCOM'])
plt.title('Possible strongly correlated stock with NVDA')
plt.show()


plt.figure(figsize=(15, 10))
heat = sns.heatmap(data.corr(),annot=True)
plt.title('heat map')
plt.show()

