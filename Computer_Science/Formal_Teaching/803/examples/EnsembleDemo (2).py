from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
clf = AdaBoostClassifier(n_estimators=10)
clf.fit(X, y)
predC = clf.predict(X)
print("Accuracy:", round(accuracy_score(y, predC)*100), "%")

# The number of weak learners is controlled by the parameter n_estimators. 
# By default, weak learners are decision stumps. Different weak learners can be specified through the base_estimator parameter.

# Import Support Vector Classifier
from sklearn.svm import SVC
clf = AdaBoostClassifier(n_estimators=10, base_estimator=SVC(probability=True))
clf.fit(X, y)
predC = clf.predict(X)
print("Accuracy:", round(accuracy_score(y, predC)*100), "%")