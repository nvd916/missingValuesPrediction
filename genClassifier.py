import numpy as np

classList = np.loadtxt('classList.txt', dtype='int')
instances = np.loadtxt('instances.txt')
test = np.loadtxt('test-cleaned.txt')

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() # Naive Bayes Classifier
clf.fit(instances, classList) # Train the data

# Make prediction for the test instances using the classifier
predicted = clf.predict(test)

# Save to file
np.savetxt('prediction.txt', predicted, fmt='%1d')

''' 
# Accuracy when testing on training data

from sklearn.metrics import accuracy_score
accuracy_score(classList, clf.predict(instances)) * 100

For now result is a sad 63.42%. 
'''
