# What is Machine Learning?

## what is MAchine Learning?

Two definitions of Machine Learning are offered. Arthur Samuel described it as: "the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.
Tom Mitchell provides a more modern definition: **"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."**
Example: playing checkers.
E = the experience of playing many games of checkers
T = the task of playing checkers.
P = the probability that the program will win the next game.
In general, any machine learning problem can be assigned to one of two broad classifications:
Supervised learning and Unsupervised learning.

경험(E)이 증가함에 따라 작업(T)을 수행하는 성능(P)이 향상될 수 있다.
(experience, task, performance)

# Supervised Learning (지도 학습)

## Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
**Supervised learning problems are categorized into "regression" and "classification" problems.** In a regression problem, we are trying to predict results within a continuous output, meaning that **we are trying to map input variables to some continuous function.** In a classification problem, we are instead trying to predict results in a discrete output. In other words, **we are trying to map input variables into discrete categories.**

**Example 1:**
Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.
We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

**Example 2:**
(a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture
(b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign. 

지도 학습: 데이터로부터 하나의 함수를 유추하기 위한 기계 학습 (회귀 문제, 분류 문제)
- 회귀 문제: 연속된 출력 내에서 결과를 예측 ex) 가격
- 분류 문제: 이산적인 범주 내에서 결과를 예측 ex) Yes or No
  
# Unsupervised Learning (비지도 학습)

## Unsupervised Learning

Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
**We can derive this structure by clustering the data based on relationships among the variables in the data.**
With unsupervised learning there is no feedback based on the prediction results.
Example:
Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.
Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

비지도 학습: 함수와 같은 구조를 유추하지 못할 때 사용 하는 기계 학습
- 데이터의 변수들 사이의 관계를 clustering하여 구조 추출, 결과의 예측보단 그룹을 나눠서 유형을 정하는 기법 (clustering: 그룹으로 묶기)

# Model and Cost Function

## Model Representation

To establish notation for future use, we’ll use x^(i) to denote the “input” variables (living area in this example), also called input features, and y^(i) to denote the “output” or target variable that we are trying to predict (price). 
A pair (x^(i) , y^(i)) is called a training example, and the dataset that we’ll be using to learn—a list of m training examples {(x^{(i)} , y^{(i)} ); i = 1, . . . , m—is called a training set. Note that the superscript “(i)” in the notation is simply an index into the training set, and has nothing to do with exponentiation. We will also use X to denote the space of input values, and Y to denote the space of output values. In this example, X = Y = ℝ.

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. Seen pictorially, the process is therefore like this:

![image](https://user-images.githubusercontent.com/79196616/110484329-e6c34380-812d-11eb-9cf9-8bbf2bce50ba.png)

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression problem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.


![image](https://user-images.githubusercontent.com/79196616/111905884-4c4df300-8a91-11eb-82c1-ab481f325cd5.png)

- m: 학습 예제의 수
- x: 종종 특징(feature)이라고 부르는 입력 변수를 표시하기 위해 사용
- y: 출력값이나 예측하려하는 목표변수를 표기하는데 사용
- (x, y)는 하나의 학습예제를 표기하는데 사용, (x(i), y(i))는 i번째 학습예제를 의미  

![image](https://user-images.githubusercontent.com/79196616/111906130-705e0400-8a92-11eb-8c60-62ff515b3f88.png)

결과값(가설) -> x 값으로 입력 받은 것을 y로 바꾸는데에 사용하는 지도   
h를 표현하는 방법

h(x)를 통해서 x의 직선 함수인 y를 예측   
선형회귀:  선형회귀의 값은 하나이며 이값은 x이다. 하나의 값 x로 모든 가격을 예측한다.   
  -> 다른말로 단일변량 선형 회귀라 한다. (단일변량은 하나의 값이라는 뜻이다.)

# Cost Function (비용 함수)

We can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.   

![image](https://user-images.githubusercontent.com/79196616/112155262-784fac80-8c28-11eb-8b1e-c92bf1c07422.png)

![image](https://user-images.githubusercontent.com/79196616/112155285-7e458d80-8c28-11eb-8689-474cda40ca0c.png)

h(x) = θ0 +θ1x 이고 여기서 최소값은 두함수의 차의 제곱을 각 training exampls의 값 마다 더해주는 것과 같다.
최소화 및 보기 쉽게 하기위해 1/2m을 해주고 이를 J라는 최소화 함수로 정의 할 수 있다.
