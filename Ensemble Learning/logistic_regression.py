#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
from collections import Counter


# In[26]:

predictions = []

head = ['variance', 'skewness', 'curtosis', 'entropy', 'class_label']


# In[27]:


test_df = pd.read_csv('test.txt', names=head)
train_df = pd.read_csv('train.txt', names=head)


# In[28]:


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# In[29]:


def calc_cost(theta, x, y):
# cost -- negative log-likelihood cost for logistic regression
    m = x.shape[0]
    y_hat = sigmoid(np.dot(theta.T, x))
    cost = (-1 / m) * (np.dot(y, np.log(y_hat).T) + np.dot((1 - y), np.log(1 - y_hat).T))
    return cost


# In[30]:


def gradient_descent(theta, x, y):
    m = x.shape[0]
    y_hat = sigmoid(np.dot(theta.T, x))
    dtheta = (1 / m) * (np.dot(x, (y_hat - y).T))
    return dtheta


# In[31]:


def predict(theta, x, y):
    m = x.shape[0]
    y_pred = np.empty((y.shape[0], y.shape[1]))
    y_hat = sigmoid(np.dot(theta.T,x))
    for i in range(y_hat.shape[1]):
        if(y_hat[0][i] < 0.5):
            y_pred[0][i] = 0
        else:
            y_pred[0][i] = 1
    return y_pred


# In[32]:


# test data
x_test = np.array(test_df.iloc[:, : -1]).T
y_test = np.array(test_df.iloc[:, -1]).reshape((60,1)).T
# Weights
theta = np.zeros((x_test.shape[0],1)) 


# In[33]:


num = int(input("Enter the number of times you want to run the program: ")) # = int(input('Enter the number of times you want to run the program: '))
k = 400


# In[34]:


costs=[]
learning_rate = 0.01

for iterr in range(num):
    # Sampling data
    sampled_data = train_df.sample(n=k, random_state=1)
    x_sample = np.array(sampled_data.iloc[:, : -1]).T
    y_sample = np.array(sampled_data.iloc[:, -1]).reshape((400,1)).T
    
    print("For Sample %i" %(iterr+1))
    # Calculating cost and gradient
    for i in range(20):
        # Calculating cost and gradient
        cost = calc_cost(theta, x_sample, y_sample)
        dtheta = gradient_descent(theta, x_sample, y_sample)
        # Updating weights
        theta = theta - learning_rate*dtheta

        if i%10==0:
            costs.append(cost)
        if i%10==0:
            cost = np.squeeze(cost)
            print("Cost after %i iterations: %f" %(i, cost))

y_pred = predict(theta, x_test, y_test).T
for length in range(len(y_pred)):
    predictions.append(int(y_pred[length]))


# In[35]:

y_test = y_test.T
print(predictions)


# In[36]:


count=0
accuracy=0
for i in range(y_pred.shape[0]):
    if(int(y_pred[i][0])==y_test[i][0]):
        count = count + 1
accuracy = (count/y_test.shape[0])*100
print("The accuracy with respect to the bagging Logistic regression is: ", accuracy)


# In[ ]:





# In[ ]:




