#!/usr/bin/env python
# coding: utf-8

# In[26]:


# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import seaborn as sns # 그래프2
import pandas as pd
import os


# In[27]:


DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['sepal length (cm)','sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class'] # iris 데이터의 Column List


# In[28]:


def fetch_iris_data(): # data 폴더와 iris의 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'iris.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_iris_data(): # iris data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'iris.csv')
    return pd.read_csv(csv_path, names=ColumnList)


# In[32]:


fetch_iris_data()
iris = load_iris_data()

ClassList = iris['class'].unique() #class의 List (꽃 종류)


# In[33]:


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
plt.axis([0,5,0,5])
plt.grid(True)
plt.legend(ClassList, loc='best')

plt.show()

