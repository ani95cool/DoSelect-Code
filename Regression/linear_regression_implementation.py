#program 1a
import numpy as np
import pandas as pd

T = { ((0.8552, 1.8292), 11.5848), ((2.6248, 2.3993), 17.6138),((8.0101, 8.8651), 54.1331), ((0.2922, 0.2867), 5.7326),((9.2885, 4.8990), 46.3750), ((7.3033, 1.6793), 29.4356),((4.8861, 9.7868), 46.4227), ((5.7853, 7.1269), 40.7433),((2.3728, 5.0047), 24.6220), ((4.5885, 4.7109), 29.7602) }

d = dict(T)
point = []
gender = []
for k, v in d.items():
	point.append(k)
	gender.append(v)	

#loading the data into the dataframe
df = pd.DataFrame(point, columns = ['x1', 'x2'])
df.insert(2, 'y', value=gender)

#plt.plot(x_train, y_train, 'x')
#plt.show()
'''
k = int(input("Enter the order of your polynomial: "))
x_values = [point for point in x_train[:k+1]]
p = np.poly1d(x_values)
'''
x_train = []
x2_train = []
y_train = []
values = []

global x_test
global theta


X1 = df['x1']
X2 = df['x2']
y = df['y']
k = int(input("Enter the order of your polynomial: "))

for sums in range(len(X1)):
	x_train.append(X1[sums])


for lines in range(len(X2)):
	x2_train.append(X2[lines])

for x in range(len(y)):
	y_train.append(y[x])

def cost_compute(x1_test):
	#print(x1_test)
	theta = np.ones(x1_test.shape)
	#print(y_test)
	hypothesis = theta.T * x1_test
	return hypothesis



def gradient_descent(x_test, y_train):
	val = cost_compute(x_test)
	t1 = 0

	length = len(x_test)

	for ln in range(length):
		t1 += (cost_compute(x_test[ln] - y_train[ln]) ** 2)

	return t1 / (2 * length)


for i in range(len(x_train)):
	for j in range(len(x2_train)):
		if(k == 1):
			x1_test = np.array([1, x_train[i], x2_train[j]])
			myval = gradient_descent(x1_test, y_train)
			p = np.poly1d(x1_test)
			val = p(myval)
			values.append(val)
		elif(k == 2):
			x1_test = np.array([1, x_train[i], x2_train[j], (x_train[i] ** 2), (x2_train[j] ** 2), (x_train[i] * x2_train[j])])
			#print(x_test)
			myval = gradient_descent(x1_test, y_train)
			p = np.poly1d(x1_test)
			val = p(myval)
			values.append(val)	
		elif(k == 3):
			x1_test = np.array([1, x_train[i], x2_train[j], (x_train[i] ** 3),(x2_train[j]**3),((x_train[j] ** 2) * x2_train[j]), (x_train[i] * (x2_train[j] ** 2))])
			myval = gradient_descent(x1_test, y_train)
			p = np.poly1d(x1_test)
			val = p(myval)
			values.append(val)	
		else:
			quit()

print(values)


	








		
