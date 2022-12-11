import numpy as np
import matplotlib.pyplot as plt 

X = np.array([55,60,65,70,75,80])
y = np.array([316,292,268,246,227,207])


# Building the model
beta0 = 0
beta1 = 0

a = 0.00001  # learning rate alpha

n_iterations = 100000
# Performing Gradient Descent 
for i in range(n_iterations):
    y_pred = beta0 + beta1*X  # The predicted value of y
    D_beta0 = (-2) * sum(y - y_pred)  # Derivative wrt beta0
    D_beta1 = (-2) * sum(X * (y - y_pred))  # Derivative wrt beta1
    beta0 = beta0 - a * D_beta0  # Update m
    beta1 = beta1 - a * D_beta1  # Update c
        
    print ('iteration ', i, ', beta0=', beta0, ', beta1 =', beta1)
    
    
# Plot results
y_pred = beta0 + beta1*X
plt.scatter(X, y) 
plt.plot(X, y_pred, color='red')  # regression line
plt.show()