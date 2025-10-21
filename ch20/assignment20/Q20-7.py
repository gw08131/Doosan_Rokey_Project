# Q20-7.py  

import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

X = pd.DataFrame({"X":x})

X = sm.add_constant(X)
model = sm.OLS(y,X).fit()

b0 = model.params['X']
b1 = model.params["const"]

# y= b0x+b1
x_line = [min(x), max(x)]
y_line = [b0*x_line[0]+b1,b0*x_line[1]+b1]

plt.scatter(x,y,color="blue")
plt.plot(x_line,y_line,linestyle='-',color="red")
plt.title("Linear Regression")
plt.show()