# **Decision Trees in sklearn**
In this section, you'll use decision trees to fit a given sample dataset.

Before you do that, let's go over the tools required to build this model.

For your decision tree model, you'll be using scikit-learn's Decision Tree Classifier class. This class provides the functions to define and fit the model to your data.

`>>> from sklearn.tree import DecisionTreeClassifier
>>> model = DecisionTreeClassifier()
>>> model.fit(x_values, y_values)`
In the example above, the model variable is a decision tree model that has been fitted to the data x_values and y_values. Fitting the model means finding the best tree that fits the training data. Let's make two predictions using the model's predict() function.

`>>> print(model.predict([ [0.2, 0.8], [0.5, 0.4] ]))
[[ 0., 1.]]`
The model returned an array of predictions, one prediction for each input array. The first input, [0.2, 0.8], got a prediction of 0.. The second input, [0.5, 0.4], got a prediction of 1..

# Hyperparameters
When we define the model, we can specify the hyperparameters. In practice, the most common ones are

`max_depth:` The maximum number of levels in the tree.
`min_samples_leaf`: The minimum number of samples allowed in a leaf.
`min_samples_split`: The minimum number of samples required to split an internal node.
## For example, here we define a model where the maximum depth of the trees max_depth is 7, and the minimum number of elements in each leaf min_samples_leaf is 10.

`>>> model = DecisionTreeClassifier(max_depth = 7, min_samples_leaf = 10)`
