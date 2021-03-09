# 1. 신경망

## 신경세포

여러개의 수상돌기에서 **자극이 합해져서 그 값이 어느 값 이상일 경우** 축색돌기로 자극을 발생시킨다.
![image](https://user-images.githubusercontent.com/79196616/110470446-339f1e00-811e-11eb-9732-4df1348abeca.png)
![image](https://user-images.githubusercontent.com/79196616/110470823-af996600-811e-11eb-97d4-85701981a085.png)

가중치와 입력값의 곱이 더해져서 학습 하는것이 신경세포의 역할과 비슷하다.

## 퍼셉트론 (Perceptron)

신경세포의 경우 어느 `임계값` 이상의 자극에만 신호를 전달한다.
학습도 마찬가지로 `임계값`의 개념을 추가한다.
![image](https://user-images.githubusercontent.com/79196616/110471293-5251e480-811f-11eb-8636-c1d1cea033b6.png)

이 단위를 **퍼셉트론 (Perceptron)** 이라고 칭함 ->선형 분리의 문제를 해결 가능함

## 퍼셉트론의 한계

하지만 간단한 XOR도 못한다.
선형분리가 불가능한 것은 풀지 못한다.
XOR는 선형분리로 풀지 못하는 문제이다.
![image](https://user-images.githubusercontent.com/79196616/110471469-81685600-811f-11eb-8d5d-f8331cbce7fa.png)

## 선형 분리 여부

![image](https://user-images.githubusercontent.com/79196616/110471539-9644e980-811f-11eb-9755-5a8490a44a3b.png)

왼쪽은 선형분리 / 오른쪽은 선으로 분류를 하기 어려움

## 선형 분리 불가 문제의 해결법

- 입력 차원을 늘린다. (사과 예)
- 입력을 비선형 변환 하여 선형분리 가능하도록 한다.
![image](https://user-images.githubusercontent.com/79196616/110471703-c7251e80-811f-11eb-8354-f99bd84f95ef.png)

- 혹은 MLP

STOP (4:37)
