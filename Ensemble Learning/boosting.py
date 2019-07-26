import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

train_data_headers = ['variance', 'skewness', 'curtoisis', 'entropy', 'class_label']
train_df = pd.read_csv('train.txt', names=train_data_headers)

X_train = train_df.iloc[:, : -1]
y_train = train_df.iloc[:, -1]
test_df = pd.read_csv('test.txt', names=train_data_headers)


X_test = test_df.iloc[:, : -1]
y_test = test_df.iloc[:, -1]

n = int(input("Enter the number of times you want: "))
model1 = LogisticRegression()
model2 = LogisticRegression()
model3 = LogisticRegression()

m1 = model1.fit(X_train, y_train)
m2 = model2.fit(X_train, y_train)
m3 = model3.fit(X_train, y_train)

m1_score = m1.score(X_test, y_test)
m2_score = m2.score(X_test, y_test)
m3_score = m3.score(X_test, y_test)

adb = AdaBoostClassifier(LogisticRegression(), n_estimators = n, learning_rate = 0.01)
fit_model = adb.fit(X_train, y_train)
adaboost_score = adb.score(X_test, y_test)
new_score = adaboost_score * 100
print("The accuracy for the three models are: ", new_score)
