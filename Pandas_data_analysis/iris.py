import urllib.request as req
import matplotlib.pyplot as plt
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
IRIS_PATH = os.path.join('data')
indexList = ['sepal length in cm','sepal width in cm', 'petal length in cm', 'petal width in cm', 'class']

def fetch_iris_data():
    if not os.path.isdir(IRIS_PATH):
        os.makedirs(IRIS_PATH)
    csv_path = os.path.join(IRIS_PATH,'iris.csv')
    req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_iris_data():
    csv_path = os.path.join(IRIS_PATH,'iris.csv')
    return pd.read_csv(csv_path, names=indexList)

fetch_iris_data()
iris = load_iris_data()
iris.hist(bins=50, figsize=(20,15))
plt.show()
