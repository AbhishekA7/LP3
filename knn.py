import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

dataset=pd.read_csv("D:\\Knn.csv")
print(dataset.head())

x=dataset[['X','Y']]
y=dataset['class']
print("")
print(x)
print("")
print(y)
print("")

classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x,y)
print("Model Trained Successfully!!!")

test=np.array([6,6])
pred=classifier.predict([test])
print("Prediction is ",pred)