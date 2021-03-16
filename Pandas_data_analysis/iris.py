# C:\Users\mpoli\Desktop\Git\pandas
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
IRIS_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['sepal length (cm)','sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class'] # iris 데이터의 Column List

def fetch_iris_data(): # data 폴더와 iris의 데이터 csv 파일 생성
    if not os.path.isdir(IRIS_PATH):
        os.makedirs(IRIS_PATH)
    csv_path = os.path.join(IRIS_PATH,'iris.csv')
    req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_iris_data(): # iris data의 csv파일을 return하는 함수
    csv_path = os.path.join(IRIS_PATH,'iris.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_iris_data()
iris = load_iris_data()

ClassList = iris['class'].unique() #class의 List (꽃 종류)

print('\n-----------------<Average value for each class>-----------------') #class 별 평균 값
print(iris.groupby('class').mean())

print('\n-----------------<Max value for each class>-----------------') #class 별 최대 값
print(iris.groupby('class').max())

print('\n-----------------<Min value for each class>-----------------') #class 별 최소 값
print(iris.groupby('class').min())

print('\n-----------------<Describe of',ColumnList[0],'>-----------------') # 꽃받침 길이의 특정 값들 정렬
print(iris.groupby(ColumnList[4])[ColumnList[0]].describe())

print('\n-----------------<Describe of',ColumnList[1],'>-----------------') # 꽃받침 너비의 특정 값들 정렬
print(iris.groupby(ColumnList[4])[ColumnList[1]].describe())

print('\n-----------------<Describe of',ColumnList[2],'>-----------------') # 꽃잎에 길이의 특정 값들 정렬
print(iris.groupby(ColumnList[4])[ColumnList[2]].describe())

print('\n-----------------<Describe of',ColumnList[3],'>-----------------') # 꽃잎에 너비의 특정 값들 정렬
print(iris.groupby(ColumnList[4])[ColumnList[3]].describe())

plt.subplot(121)
for flower in ClassList:
    flowerList = iris[iris['class']==flower]
    plt.plot(flowerList[ColumnList[2]], flowerList[ColumnList[0]], 'o')

plt.xlabel(ColumnList[2])
plt.ylabel(ColumnList[0])
plt.axis([0,9,0,9])
plt.grid(True)
plt.legend(ClassList, loc='best')

plt.subplot(122)
for flower in ClassList:
    flowerList = iris[iris['class']==flower]
    plt.plot(flowerList[ColumnList[3]], flowerList[ColumnList[1]], 'o')

plt.xlabel(ColumnList[3])
plt.ylabel(ColumnList[1])
plt.axis([0,9,0,9])
plt.grid(True)
plt.legend(ClassList, loc='best')

plt.show()
