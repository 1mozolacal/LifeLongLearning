from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt 

X = np.array([55,60,65,70,75,80]).reshape(-1, 1)
y = np.array([316,292,268,246,227,207]).reshape(-1, 1)

scalerX = StandardScaler()
scalerX.fit(X)
scalerY = StandardScaler()
scalerY.fit(y)
xScaled = scalerX.transform(X)
yScaled = scalerY.transform(y)

# Building the model
beta0 = 0
beta1 = 0

a = 0.0001  # learning rate alpha

n_iterations = 1000
# Performing Gradient Descent 
for i in range(n_iterations):
    y_pred = beta0 + beta1*xScaled  # The predicted value of y
    D_beta0 = (-2) * sum(yScaled - y_pred)  # Derivative wrt beta0
    D_beta1 = (-2) * sum(xScaled * (yScaled - y_pred))  # Derivative wrt beta1
    beta0 = beta0 - a * D_beta0  # Update m
    beta1 = beta1 - a * D_beta1  # Update c
        
    print ('iteration ', i, ', beta0=', beta0, ', beta1 =', beta1)
    
    
# Plot results
y_pred = beta0 + beta1*xScaled
plt.scatter(X, y) 
plt.plot(X, scalerY.inverse_transform(y_pred), color='red')  # regression line
plt.show()



