import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize

# Load the data
ccDefault = pd.read_csv(r'C:\users\elodi\Desktop\ccdefault.csv') 

# Pre-process the data
X = ccDefault.drop(['ID','DEFAULT'], axis = 1)
y = ccDefault['DEFAULT']
X = normalize(X)

# Split the data
XTrain, XTest, yTrain, yTest = train_test_split(X,y, test_size=0.3)

# Conduct KNN classification
clf = KNeighborsClassifier(n_neighbors=5)

# Train  classifier
clf.fit(XTrain, yTrain)

# Predict labels
yTestPred = clf.predict(XTest)

# Print the accuracy of the classifier
print("The accuracy of the classifer is", round(accuracy_score(yTest, yTestPred)*100), '%')