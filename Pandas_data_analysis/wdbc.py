# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean', 'points_mean', 'symmetry_mean', 'dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
'compactness_se', 'concavity_se', 'points_se', 'symmetry_se', 'dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'points_worst', 'symmetry_worst', 'dimension_worst'] # wdbc 데이터의 Column List

def fetch_wdbc_data(): # data 폴더와 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'wdbc.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_wdbc_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'wdbc.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_wdbc_data()
wdbc = load_wdbc_data()

print('\n-----------------<Average>-----------------')
print(wdbc.groupby('diagnosis').mean())

print('\n-----------------<Max>-----------------')
print(wdbc.groupby('diagnosis').max())

print('\n-----------------<Min>-----------------')
print(wdbc.groupby('diagnosis').min())