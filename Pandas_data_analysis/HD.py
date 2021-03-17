# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['age', 'sex', ' chest pain type', 'resting blood pressure', 'serum cholestoral in mg/d', 'fasting blood sugar > 120 mg/dl', 'resting electrocardiographic results', 'maximum heart rate achieved', 'exercise induced angina', 'oldpeak = ST depression induced by exercise relative to rest', 'the slope of the peak exercise ST segment', 'number of major vessels (0-3) colored by flourosopy', 'thal', 'target']

def fetch_HD_data(): # data 폴더와 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'HD.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_HD_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'HD.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_HD_data()
HD = load_HD_data()

print('\n----------------------<mean>----------------------')
print(HD.groupby('target').mean())
print('\n----------------------<max>----------------------')
print(HD.groupby('target').max())
print('\n----------------------<min>----------------------')
print(HD.groupby('target').min())
print('\n----------------------<target mean>----------------------')
print(HD.groupby('target').mean())