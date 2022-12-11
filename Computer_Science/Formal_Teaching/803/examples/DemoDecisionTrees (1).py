import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the wine.csv data
data = pd.read_csv(r"C:\Users\...\wine.csv", header = None)

# Split the data for training and testing
train, test = train_test_split(data, test_size=0.3)

# Extract the target class
y_train = train.iloc[:,0]
y_test = test.iloc[:,0]
# Extract the data features
X_train = train.iloc[:,1:]
X_test = test.iloc[:,1:]

# Create the decision tree classifier
clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 3)
clf = clf.fit(X_train, y_train)

# Apply the decision tree to classify the test data
y_test_pred = clf.predict(X_test)

print("The accuracy of the classifier is", accuracy_score(y_test, y_test_pred))