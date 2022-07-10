# 신경망 - 완성본

import numpy as np


def sigmoid(x):                 # 시그모이드 함수
    return 1 / (1 + np.exp(-x))
        
    
def identity_function(x):       # 항등 함수
    return x


def init_network():             # 네트워크 초기화 및 선언 initialize
    network = {}
    network['w1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['w2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['w3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network              # 반환
    
 
def forward(network, x):        # 정방향
    w1, w2, w3 = network['w1'], network['w2'], network['w3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3'] 
    
    a1 = np.dot(x, w1) + b1     # (1X2) X (2X3) + 1X3 = 1X3
    z1 = sigmoid(a1)            # 은닉 1층
    
    a2 = np.dot(z1, w2) + b2    # (1X3) X (3X2) + 1X2 = 1X2
    z2 = sigmoid(a2)            # 은닉 2층

    a3 = np.dot(z2, w3) + b3    # (1X2) X (2X2) + 1X2 = 1X2

    y = identity_function(a3)   # 3층 - 출력층
    
    return y
    

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)                        # [0.31682708 0.69627909]