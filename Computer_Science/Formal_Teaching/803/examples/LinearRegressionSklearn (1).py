import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
X = np.load(r"C:/Users/elodi/Desktop/Xdata.npy")
y = np.load(r"C:/Users/elodi/Desktop/Ydata.npy")

# Visualize the data
plt.scatter(X, y, color='black')
plt.xlabel('X')
plt.ylabel('y')

# Split the instances into a training and test set
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2)

# Perform the linear regression
reg = linear_model.LinearRegression()
reg.fit(xTrain, yTrain)

# Plot the linear fit
yPred = reg.predict(X)
plt.scatter(X, yPred, color='r')

# Model evaluation on the test set
yTestPred = reg.predict(xTest)

# Print the mean squared error of the predictions on the test set
print("The mean squared error", mean_squared_error(yTest, yTestPred))