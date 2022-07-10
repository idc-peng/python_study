# ReLU(Rectified Linear Unit) 함수

import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)
    
x = np.arange(-1.0, 1.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()