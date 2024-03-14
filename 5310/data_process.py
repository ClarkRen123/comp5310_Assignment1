import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import warnings
import pickle
warnings.simplefilter(action='ignore', category=FutureWarning)


# read all data
NVDA = pd.read_csv('datasets/NVIDIA (1999 -11.07.2023).csv')
AMD = pd.read_csv('datasets/AMD (1980 -11.07.2023).csv')
ASML = pd.read_csv('datasets/ASML.csv')
BTC = pd.read_csv('datasets/BTC-USD (2014-2024).csv')
ETH = pd.read_csv('datasets/ETH-USD (2017-2024).csv')
QCOM = pd.read_csv('datasets/QCOM.csv')
TXN = pd.read_csv('datasets/TXN.csv')
INTEL = pd.read_csv('datasets/INTEL (1980 - 11.07.2023).csv')
# these two are complicated and need special processing
benchmark = pd.read_csv('datasets/GPU_benchmarks_v7.csv') # abnormal: years only
NASDAQ = pd.read_csv('datasets/Stock Market Dataset.csv') # abnormal: Date in DD/MM/YY format


# clean all data so that only data from 2018 to 2022 remain
start_date = pd.to_datetime('2017-12-31')
end_date = pd.to_datetime('2022-12-31')
# formating and sorting


def form(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df_sorted = df.sort_values(by='Date', ascending=True)
    filtered_df = df_sorted[(df_sorted['Date'] >= start_date) & (df_sorted['Date'] <= end_date)]
    return filtered_df

def form_NASDAQ(df):
    df['Date'] = pd.to_datetime(df['Date'],dayfirst = True)
    df_sorted = df.sort_values(by='Date', ascending=True)
    filtered_df = df_sorted[(df_sorted['Date'] >= start_date) & (df_sorted['Date'] <= end_date)]
    return filtered_df

#for benchmark, we need to consider NVIDIA-made GPU performances and other GPUs
def form_benchmark(df):
    df_sorted = df.sort_values(by='Date', ascending=True)
    filtered_df_1 = df_sorted[(df_sorted['Date'] == 2017)]
    filtered_df_2 = df_sorted[(df_sorted['Date'] == 2018)]
    filtered_df_3 = df_sorted[(df_sorted['Date'] == 2019)]
    filtered_df_4 = df_sorted[(df_sorted['Date'] == 2020)]
    filtered_df_5 = df_sorted[(df_sorted['Date'] == 2021)]
    filtered_df_6 = df_sorted[(df_sorted['Date'] == 2022)]
    return (filtered_df_1, filtered_df_2, filtered_df_3, filtered_df_4, filtered_df_5, filtered_df_6)

def selectGpu(df,y):
    Ncounter = 0
    Ocounter = 0
    G3DNV = []
    G3DO = []
    for i in df['gpuName']:
        rows = df[df['gpuName'] == i].index
        cindex = df.columns.get_loc('gpuName')
        if (('Tesla' in i or 'GRID' in i or 'GeForce' in i or 'Quadro' in i or 'Titan' in i or 'RTX' in i)
                or i[0] == 'T' or i[0] == 'P' or (i[0] == 'A' and i[1] != 'S')):
            Ncounter += 1
            G3DNV.append(int(df.loc[rows,'G3Dmark']))

        else:
            Ocounter+=1
            G3DO.append(int(df.loc[rows,'G3Dmark']))
    return [y, Ncounter, statistics.median(G3DNV), max(G3DNV), Ocounter, statistics.median(G3DO), max(G3DO)]


NVDA = form(NVDA)
AMD = form(AMD)
ASML = form(ASML)
BTC = form(BTC)
ETH = form(ETH)
QCOM = form(QCOM)
TXN = form(TXN)
INTEL = form(INTEL)
NASDAQ = form_NASDAQ(NASDAQ)
b17,b18,b19,b20,b21,b22 = form_benchmark(benchmark)
d17 = selectGpu(b17,2017)
d18 = selectGpu(b18,2018)
d19 = selectGpu(b19,2019)
d20 = selectGpu(b20,2020)
d21 = selectGpu(b21,2021)
d22 = selectGpu(b22,2022)
df_b = pd.DataFrame([d17,d18,d19,d20,d21,d22], columns=['Year','NVIDIA GPU release', 'NVIDIA meidan performance', 'NVIDIA maximum performance',
                                                      'other GPU release','other meidan performance', 'other maximum performance'])
NVR = NVP1 = NVP2 = OTR = OTP1 = OTP2 = []

s2018 = NVDA[NVDA['Date'].between(pd.to_datetime('2018-01-01'),pd.to_datetime('2019-01-01'))]['Date'].count()
s2019 = NVDA[NVDA['Date'].between(pd.to_datetime('2019-01-01'),pd.to_datetime('2020-01-01'))]['Date'].count()
s2020 = NVDA[NVDA['Date'].between(pd.to_datetime('2020-01-01'),pd.to_datetime('2021-01-01'))]['Date'].count()
s2021 = NVDA[NVDA['Date'].between(pd.to_datetime('2021-01-01'),pd.to_datetime('2022-01-01'))]['Date'].count()
s2022 = NVDA[NVDA['Date'].between(pd.to_datetime('2022-01-01'),pd.to_datetime('2023-01-01'))]['Date'].count()
#print(s2018+s2019+s2020+s2021+s2022)




NVR = NVR + [d18[1]]*s2018 + [d19[1]]*s2019 + [d20[1]]*s2020 + [d21[1]]*s2021 + [d22[1]]*s2022
NVP1 = NVP1 + [d18[2]]*s2018 + [d19[2]]*s2019 + [d20[2]]*s2020 + [d21[2]]*s2021 + [d22[2]]*s2022
NVP2= NVP2 + [d18[3]]*s2018  + [d19[3]]*s2019 + [d20[3]]*s2020 + [d21[3]]*s2021 + [d22[3]]*s2022
OTR = OTR + [d18[4]]*s2018 + [d19[4]]*s2019 + [d20[4]]*s2020 + [d21[4]]*s2021 + [d22[4]]*s2022
OTP1 = OTP1 + [d18[5]]*s2018 + [d19[5]]*s2019 + [d20[5]]*s2020 + [d21[5]]*s2021 + [d22[5]]*s2022
OTP2 = OTP2 + [d18[6]]*s2018 + [d19[6]]*s2019 + [d20[6]]*s2020 + [d21[6]]*s2021 + [d22[6]]*s2022




# concatenation of all data
# use open prices of rivalry companies each day, count open prices and volumes of BTC and ETH each day

AMD = AMD[['Open']].rename(columns={'Open': 'AMD'})
ASML = ASML[['Open']].rename(columns={'Open': 'ASML'})
QCOM = QCOM[['Open']].rename(columns={'Open': 'QCOM'})
TXN = TXN[['Open']].rename(columns={'Open': 'TXN'})
INTEL = INTEL[['Open']].rename(columns={'Open': 'INTEL'})
BTC.rename(columns={'Open': 'BTC', 'Volume': 'BTC-Volume'}, inplace=True)
ETH.rename(columns={'Open': 'ETH', 'Volume': 'ETH-Volume'}, inplace=True)
#print(NVDA)
NVDA.reset_index(drop=True, inplace=True)
AMD.reset_index(drop=True, inplace=True)
ASML.reset_index(drop=True, inplace=True)
QCOM.reset_index(drop=True, inplace=True)
TXN.reset_index(drop=True, inplace=True)
INTEL.reset_index(drop=True, inplace=True)

result_df = pd.concat([NVDA, AMD,ASML,QCOM,TXN,INTEL],  axis=1)
#
result_df = pd.merge(result_df, BTC[['Date', 'BTC', 'BTC-Volume']], on='Date', how='left')
#print(result_df)
result_df = pd.merge(result_df, ETH[['Date', 'ETH', 'ETH-Volume']], on='Date', how='left')

result_df['NVIDIA release'] = NVR
result_df['NVIDIA median performance'] = NVP1
result_df['NVIDIA maximum performance'] = NVP2
result_df['others release'] = OTR
result_df['others median performance'] = OTP1
result_df['others maximum performance'] = OTP2
print(result_df)

# save
file_path = 'data.pickle'

with open(file_path, 'wb') as file:
    pickle.dump(result_df, file)






