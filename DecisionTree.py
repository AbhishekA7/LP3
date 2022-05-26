#import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

#reading Dataset
dataset=pd.read_csv("D:\\data.csv")
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,5].values

#Perform Label encoding
labelencoder_X = LabelEncoder()
X = X.apply(LabelEncoder().fit_transform)
print (X)

regressor=DecisionTreeClassifier()
regressor.fit(X.iloc[:,1:5],y)

#Predict value for the given expression
X_in=np.array([1,1,0,0])
y_pred=regressor.predict([X_in])
print ("Prediction:", y_pred)

#Plot and Show
plt.figure(figsize=(10,3))
plot_tree(regressor)
plt.show()
