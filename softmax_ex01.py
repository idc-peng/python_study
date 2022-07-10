# 소프트 맥스 함수

import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)       # 오버플로우 방지
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)                  # y 값은 확률이므로 y 리스트 값의 합은 1이다

print(y)

print(np.sum(y))