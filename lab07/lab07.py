from numpy import *

import math

import matplotlib.pyplot as plt
x = linspace(0, 5, 100)


y = cos(x*x)/x

plt.plot(x, y, 'm-')
plt.legend(['Y(x)=cos(x^2)/x, x=[0...5]'], loc='upper right')

plt.savefig('lab_7_1.png', dpi=200)









