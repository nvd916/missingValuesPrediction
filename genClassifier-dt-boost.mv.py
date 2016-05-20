import numpy as np

classList = np.loadtxt('classList.txt')
instances = np.loadtxt('instances.txt')
test = np.loadtxt('test-cleaned.txt')
# classTrue = np.loadtxt('prelim-class.txt')

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
clf = DecisionTreeClassifier() # Naive Bayes Classifier
boost_clf = AdaBoostClassifier(base_estimator = clf, algorithm = 'SAMME')
boost_clf.fit(instances, classList) # Train the data

# Make prediction for the test instances using the classifier
predicted = boost_clf.predict(test)
# predicted = boost_clf.predict(instances)

# Save to file
np.savetxt('prediction.txt', predicted, fmt='%1d')

# Persist the model
#from sklearn.externals import joblib
#joblib.dump(clf, 'gaussian.pkl')

# Accuracy when testing on training data

from sklearn.metrics import accuracy_score
# print(accuracy_score(classTrue, predicted) * 100)
# print(accuracy_score(classList, predicted) * 100)
