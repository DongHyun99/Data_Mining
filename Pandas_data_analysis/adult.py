# C:\Users\mpoli\Desktop\Git\Deeplearning\Pandas_data_analysis
import urllib.request as req # 웹에서 다운로드 할 때
import matplotlib.pyplot as plt # 그래프
import pandas as pd
import os

DOWNLOAD_ROOT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
DATA_PATH = os.path.join('data') # 데이터 저장 폴더
ColumnList = ['age', 'workclass','fnlwgt','education','education_num', 'maritial_status','occupation','relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'Earned more than 50K'] # adult 데이터의 Column List

def fetch_adult_data(): # data 폴더와 adult의 데이터 csv 파일 생성
    if not os.path.isdir(DATA_PATH):
        os.makedirs(DATA_PATH)
    csv_path = os.path.join(DATA_PATH,'adult.csv')
    if not os.path.isfile(csv_path):
        req.urlretrieve(DOWNLOAD_ROOT, csv_path)

def load_adult_data(): # data의 csv파일을 return하는 함수
    csv_path = os.path.join(DATA_PATH,'adult.csv')
    return pd.read_csv(csv_path, names=ColumnList)

fetch_adult_data()
adult = load_adult_data()

print('\n-----------------<Average>-----------------')
print(adult.groupby('Earned more than 50K').mean())

print('\n-----------------<Max>-----------------')
print(adult.groupby('Earned more than 50K').max())

print('\n-----------------<Min>-----------------')
print(adult.groupby('Earned more than 50K').min())

Fe50K = len(adult[(adult['sex']==' Female') & (adult['Earned more than 50K']==' >50K')]) / len(adult[adult['sex']==' Female'])*100
Ma50K = len(adult[(adult['sex']==' Male') & (adult['Earned more than 50K']==' >50K')]) / len(adult[adult['sex']==' Male'])*100
Feage50K = []
Maage50K = []
for i in range(10,90,10):
    Feage50K.append(len((adult[(adult['sex']==" Female") & (adult['age'] < i) & (adult['age'] >= (i-10)) & (adult['Earned more than 50K']==' >50K')])))
    Maage50K.append(len((adult[(adult['sex']==" Male") & (adult['age'] < i) & (adult['age'] >= (i-10)) & (adult['Earned more than 50K']==' >50K')])))
white = len(adult[adult['race']==' White']) / len(adult)
asian = len(adult[adult['race']==' Asian-Pac-Islander']) / len(adult)
amer = len(adult[adult['race']==' Amer-Indian-Eskimo']) / len(adult)
other = len(adult[adult['race']==' Other']) / len(adult)
black = len(adult[adult['race']==' Black']) / len(adult)

plt.subplot(221) # 여성의 50K 비율
ratio = [Fe50K, 100-Fe50K]
labels = ['Female > 50K', 'Female <=50K']
plt.pie(ratio, labels=labels, autopct='%.2f%%')
plt.title('50K ratio of female')

plt.subplot(222) # 남성의 50K 비율
ratio = [Ma50K, 100-Ma50K]
labels = ['Male > 50K', 'Male <=50K']
plt.pie(ratio, labels=labels, autopct='%.2f%%')
plt.title('50K ratio of male')

plt.subplot(223) # 나이에 따른 여자와 남자의 50K 수
plt.plot([i*10 for i in range(1,9,1)],Feage50K)
plt.plot([i*10 for i in range(1,9,1)],Maage50K)
plt.grid()
plt.title('Age of earns more than (>50K)')
plt.xlabel('Age')
plt.ylabel('Number of people')
plt.legend(['Female', 'Male'], loc='best')

plt.subplot(224)
ratio = [white, asian, amer, other, black]
labels = [' White',' Asian-Pac-Islander',' Amer-Indian-Eskimo',' Other',' Black']
plt.pie(ratio, labels=labels, autopct='%.2f%%')
plt.title('Race-specific 50K ratio')

plt.show()
