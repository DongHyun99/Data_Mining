# 1. Pandas

## Pandas의 특징

- NumPy의 특징을 그대로 가짐
- 데이터분석에 특화된 데이터 구조 제공 (Series, dataFrame)
- 다양한 데이터 분석 함수 제공 (평균, 표준편차 등)
- DB와 쉽게 연결 가능

## Pandas 학습 방법
 
가장 좋은것은 공식문서를 보는 것   
판다스를 한 장에 정리해 둔 치트시트 Data Wrangling with pandas Cheat Sheet 참조하면서 사용하기!   

![image](https://user-images.githubusercontent.com/79196616/110962317-330fbd00-8394-11eb-96a6-ce901a07a26b.png)
![image](https://user-images.githubusercontent.com/79196616/110962349-39059e00-8394-11eb-93a6-62e7e9f7cd27.png)

혹은 Python for data Analysis 문서(책) 참조하기   
Pandas는 그저 Tool일 뿐라는것을 명심   

## Pandas 사용하기

- import

```python
import pandas as pd //pandas가 너무 길기 때문에 통상 pd로 줄여서 쓴다.
import numpy as np
import matplotlib.pylot as plt
```   
  
Pandas의 모든 API는 `help()` 함수를 이용하여 도움말을 확인할 수 있다.

# 2. Pandas 데이터 구조

![image](http://drive.google.com/uc?export=view&id=1B0ZpHC2hCXfoeYKxMT4DRHqKrQbEbztj)

## Series

- 1차원 뎅터 구조
- 일반적으로 s 또는 sr로 이름붙임

![image](http://drive.google.com/uc?export=view&id=1msqZqjnrFLJXlaBGF7DsLf2B0_lA_J07)

```python
s = pd.Series([3,-5,7,4]) //index 없이 생성
```

```
0 3
1 -5
2 7
3 4
dtype: int64
```

인덱스를 특별히 지정해주지 않으면 NumPy 다차원배열처럼 0부터 인덱스가 시작된다.   
NumPy 다차원 배열과 다르게 Pandas Series는 인덱스를 지정해 줄 수 있으며 숫자가 아닌 문자열도 인덱스가 될 수 있다.   

```python
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
````

**type()** 을 통해 데이터타입이 Series인 것을 확인할 수 있음   

## 속성

Series는 index와 values를 가진다.

## 인덱싱

index명 또는 index의 순서를 통해 인덱싱할 수 있다.

