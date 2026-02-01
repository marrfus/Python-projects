from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,2,3,4,5])

model = LinearRegression()
model.fit(X, y)

print(model.coef_[0], model.intercept_)