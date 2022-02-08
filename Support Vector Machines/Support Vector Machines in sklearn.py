# Import statements 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

# Read the data.
data = np.asarray(pd.read_csv('data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 
X = data[:,0:2]
y = data[:,2]

# Create the model and assign it to the variable model.
# this parsmeters achieve 100% accuracy on the dataset.
model = SVC(kernel='rbf', gamma=60)
# u can use another parameters like but it gives 60% accuracy 
#model = SVC(kernel='poly',degree=4',C=0.2)

# Fit the model.
model.fit(X,y)

#  Make predictions. Store them in the variable y_pred.
y_pred = model.predict(X)

# Calculate the accuracy and assign it to the variable acc.
acc = accuracy_score(y_pred,y)
