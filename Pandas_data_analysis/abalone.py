# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os
import seaborn as sns

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['sex','length','diameter','height','whole weight','shucked weight', 'viscera weight', 'shell weight','rings'] # adult 데이터의 Column List

def fetch_abalone_data(): # data 폴더와 abalone의 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'abalone.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_abalone_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'abalone.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_abalone_data()
abalone = load_abalone_data()

print('\n-----------------<Average>-----------------')
print(abalone.groupby('rings').mean())

print('\n-----------------<Max>-----------------')
print(abalone.groupby('rings').max())

print('\n-----------------<Min>-----------------')
print(abalone.groupby('rings').min())

sns.pairplot(vars=['diameter', 'height','whole weight'], hue="rings", data=abalone)
plt.show()