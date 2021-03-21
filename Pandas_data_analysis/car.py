# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['buying', 'maint','doors','persons','lug_boot','safety', 'target']

def fetch_car_data(): # data 폴더와 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'car.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_car_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'car.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_car_data()
car = load_car_data()

print(car)

print('\n----------------------<describe>----------------------')
print(car.groupby('target').describe())
print('\n----------------------<max>----------------------')
print(car.groupby('target').max())
print('\n----------------------<min>----------------------')
print(car.groupby('target').min())