# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os
import seaborn as sns

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'] # wine 성분 데이터 ColumnList

def fetch_wine_data(): # data 폴더와 wine의 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'wine.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_wine_data(): # wine data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'wine.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_wine_data()
wine = load_wine_data()

print('\n----------------------<mean>----------------------')
print(wine.groupby('Class').mean())
print('\n----------------------<max>----------------------')
print(wine.groupby('Class').max())
print('\n----------------------<min>----------------------')
print(wine.groupby('Class').min())

sns.pairplot(vars=["Alcohol", "Alcalinity of ash", "Total phenols", "Flavanoids"], hue="Class", data=wine)
plt.show()