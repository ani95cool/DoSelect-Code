from scipy.optimize import *
import numpy as np
import pandas as pd
from collections import Counter

D = { ((170, 57, 32), 'W'), ((192, 95, 28), 'M'), ((150, 45, 30), 'W'), ((170, 65, 29), 'M'), ((175, 78, 35), 'M'), ((185, 90, 32), 'M'), ((170, 65, 28), 'W'), ((155, 48, 31), 'W'), ((160, 55, 30), 'W'), ((182, 80, 30), 'M'), ((175, 69, 28), 'W'), ((180, 80, 27), 'M'), ((160, 50, 31), 'W'), ((175, 72, 30), 'M')}
point = []
gender = []
name = ''
d = dict(D)
women = []
men = []
global tp
global ap
mine = []
l = []
alpha = 0.01
li = []
for k, v in d.items():
	point.append(k)
	gender.append(v)	

#loading the data into the dataframe
df = pd.DataFrame(point, columns = ['height', 'weight', 'age'])
df.insert(3, 'gender', value=gender)
x_value = df.iloc[:, :-1]

X = np.array(x_value)
print(X)	
transpose = X.T

y_value = df.iloc[:, -1]
#print(y_value)

for i in range(len(y_value)):
	if(y_value[i] == 'W'):
		women.append(1)

	elif(y_value[i] == 'M'):
		men.append(0)

	else:
		pass

n = int(input("Enter the number of samples needed: "))
for kv in range(n):
	height = int(input("Enter your height: "))
	weight = int(input("Enter your weight: "))
	age = int(input("Enter your age: "))
	l = []
	l.append(height)
	l.append(weight)
	l.append(age)

	samples = np.array(l)
	print(samples)
	new = np.reshape(samples, (3,1))
	theta = np.ones((X.shape[0], 1))
	trans = theta.T
	men.extend(women)
	y = np.array(men)

	def sigmoid(x):
		res = -1 * x
		my = np.exp(res)
		lo = my + 1
		result = 1 / lo
		return result

	def net_prod(x, mu):
		return x * mu

	def hypothesis(x, name):
		return sigmoid(net_prod(x, name))

	predictions = []

	def gradient_descent(th, x):
		m = x.shape[0]
		return (1 / m) * np.dot(x.T, sigmoid(net_prod(theta,   x)) - y)
		

	#print(X.T.shape)
	t = gradient_descent(transpose, theta)
	#print(t)
	inter = net_prod(t,new)
	#print(inter)
	sig = sigmoid(inter)
	#print(sig)
	n = len(sig)
	arr = sig[0]
	ji = sig[1]
	ki = sig[2]
	for km in range(len(ji)):
		if(ji[km] > 0.5):
			predictions.append('W')
		else:
			predictions.append('M')

	for kh in range(len(ji)):
		if(ji[kh] > 0.5):
			predictions.append('W')
		else:
			predictions.append('M')

	for kt in range(len(ji)):
		if(ji[kt] > 0.5):
			predictions.append('W')
		else:
			predictions.append('M')		
				
	pass

	#print("The predictions are: \n", predictions)


	vote_result = Counter(predictions).most_common(1)[0][0]
	print("The possible label is ", vote_result)



		

    	

#print(x1_value)




