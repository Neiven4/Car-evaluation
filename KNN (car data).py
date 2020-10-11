# IMPORTING LIBRARY
import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

# Loading data
data = pd.read_csv("car.data")
print(data.head())

# Preprosessing the categoral data
le = preprocessing.LabelEncoder()
Buying = le.fit_transform(list(data["buying"]))
Maint = le.fit_transform(list(data["maint"]))
Door = le.fit_transform(list(data["door"]))
Person = le.fit_transform(list(data["persons"]))
Lug_boot = le.fit_transform(list(data["lug_boot"]))
Safety = le.fit_transform(list(data["safety"]))
Class = le.fit_transform(list(data["class"]))

predict = "class"

x = list(zip(Buying, Maint, Door, Person, Lug_boot, Safety,))
y = list(Class)

train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.1)

# Creating the model
model = KNeighborsClassifier(n_neighbors=7)
model.fit(train_X, train_y)
acc = model.score(test_X, test_y)
print(acc)

prediction = model.predict(test_X)

# Creating pickle

with open("carmodel.pkl", "wb") as f:
    pickle.dump(model, f)

# Display result
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(prediction)):
    print("prediction: ", names[prediction[x]], "data: ", test_X[x], "Actual: ", names[test_y[x]])

