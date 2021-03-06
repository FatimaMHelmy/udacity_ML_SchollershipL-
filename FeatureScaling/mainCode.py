#  Add import statements
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('data.csv', header = None)
#visualize the data using dataFramme
df = pd.DataFrame(train_data)
print(df)
# split data into features and target 
X = train_data.iloc[:,:-1] # get all rows and all coloumns instead last one
Y=train_data.iloc [:,-1] # get all rows and last coloumn
#  Create the standardization scaling object.
scaler = StandardScaler()

#  Fit the standardization parameters and scale the data.
X_scaled = scaler.fit_transform(X)

# Create the linear regression model with lasso regularization.
lasso_reg = Lasso()

# Fit the model.
lasso_reg.fit(X_scaled, Y)
# Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)
