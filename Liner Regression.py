from statistics import mean
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(1, 100, 10)
y = 2 * x + np.random.randint(1, 30, 10)

def best_fit_line(x, y):
    slope = ((mean(x) * mean(y)) - mean(x*y)) / ((mean(x) * mean(x)) - mean(x*x))
    intercept = mean(y) - slope * mean(x)
    return slope, intercept

slope, intercept = best_fit_line(x, y)
regression_line = [(slope * x)+intercept for x in x] 

plt.scatter(x, y)
plt.plot(x, regression_line)
plt.show()

