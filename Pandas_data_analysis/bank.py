# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DATA_PATH = os.path.join('data') # 데이터 저장 폴더

def load_bank_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'bank.csv')
    return pd.read_csv(csv_path, sep=';')

bank = load_bank_data()

print('\n----------------------<mean>----------------------')
print(bank.groupby('y').mean())
print('\n----------------------<max>----------------------')
print(bank.groupby('y').max())
print('\n----------------------<min>----------------------')
print(bank.groupby('y').min())