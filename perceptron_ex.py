# 퍼셉트론 구현 단계

import numpy as np
import matplotlib.pyplot as plt


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1