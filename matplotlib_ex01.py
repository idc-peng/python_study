# matplotlib ex01

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 7, 0.1) # 0 <= x < 7
y_sin = np.sin(x)            # sin 함수
y_cos = np.cos(x)

plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, linestyle="--", label="cos")

plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')    # title 제목
plt.legend()
plt.show()
