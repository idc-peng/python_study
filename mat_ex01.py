# 신경망 - 흐름대로 구현

import numpy as np
import matplotlib.pyplot as plt

#class Function:
#    def __init__(self, name):
#        self.name = name
    
    
def sigmoid(x):                 # 시그모이드 함수
    return 1 / (1 + np.exp(-x))
        
    
def identity_function(x):       # 항등 함수
    return x

    
x = np.array([1.0, 0.5])                                # 입력층
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])       # 가중치 weight
b1 = np.array([0.1, 0.2, 0.3])                          # 편향 bias


print(x.shape)     # 1 X 2
print(w1.shape)    # 2 X 3
print(b1.shape)    # 1 X 3
print()


a1 = np.dot(x, w1) + b1         # (1X2) X (2X3) + 1X3 = 1X3
z1 = sigmoid(a1)                # 은닉 1층
#z1 = Function(a1)          

print("a1 = ", a1)              # [0.3 0.7 1.1]
print("z1 = ", z1)              # [0.57444252 0.66818777 0.75026011]
print("-" * 50)

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

print(z1.shape)     # 1 X 3
print(w2.shape)     # 3 X 2 
print(b2.shape)     # 1 X 2
print()

a2 = np.dot(z1, w2) + b2        # (1X3) X (3X2) + 1X2 = 1X2
z2 = sigmoid(a2)                # 은닉 2층

print("a2 = ", a2)              # [0.51615984 1.21402696]
print("z2 = ", z2)              # [0.62624937 0.7710107 ]
print("-" * 50)


w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

print(z2.shape)     # 1 X 2
print(w3.shape)     # 2 X 2
print(b3.shape)     # 1 X 2
print()

a3 = np.dot(z2, w3) + b3    # (1X2) X (2X2) + 1X2 = 1X2
y = identity_function(a3)   # y = h(a3)     h - 항등함수

print(y)                    # [0.31682708 0.69627909]