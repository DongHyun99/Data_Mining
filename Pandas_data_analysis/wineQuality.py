# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
DOWNLOAD_ROOT2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더

def fetch_wq_data(): # data 폴더와 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'winequality-red.csv')
    csv_path2 = os.path.join(DATA_PATH, 'winequality-white.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)
    if not os.path.isfile(csv_path2):
        req.urlretrieve(DOWNLOAD_ROOT2, csv_path2)

def load_wqr_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'winequality-red.csv')
    return pd.read_csv(csv_path, sep=';') # 구분자를 ;으로 변경

def load_wqw_data():
    csv_path = os.path.join(DATA_PATH,'winequality-white.csv')
    return pd.read_csv(csv_path, sep=';')

fetch_wq_data()
red = load_wqr_data()
white = load_wqw_data()

print('\n---------------<mean>-----------------')
print('<red>')
print(red.mean())
print('\n<white>')
print(white.mean())

print('\n---------------<max>-----------------')
print('<red>')
print(red.max())
print('\n<white>')
print(white.max())

print('\n---------------<min>-----------------')
print('<red>')
print(red.min())
print('\n<white>')
print(white.min())
