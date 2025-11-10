def function(x):
    return (x + 3) ** 2

def derivative(x):
    return 2 * (x + 3)

x = 2 
learning_rate = 0.1
precision = 0.0001 
max_iterations = 1000 

for i in range(max_iterations):
    grad = derivative(x)
    x_new = x - learning_rate * grad
    if abs(x_new - x) < precision:
        print(f"Converged at iteration {i}")
        break
    x = x_new

print(f"Local minimum occurs at x = {x}")
print(f"Function value at local minimum: y = {function(x)}")

import matplotlib as plot
import numpy as np
import sympy as sym 
from matplotlib import pyplot
x_cordinate = np.linspace(-15,15,100)
pyplot.plot(x_cordinate,function(x_cordinate))
pyplot.plot(2,function(2),'ro')
pyplot.show()