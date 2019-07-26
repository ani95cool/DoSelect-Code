#program 1b
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig1 =  plt.figure(figsize=(10, 10))
ax = Axes3D(fig1)
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)

D = {((6.4432, 9.6309), 50.9155), ((3.7861, 5.4681), 29.9852),((8.1158, 5.2114), 42.9626), ((5.3283, 2.3159), 24.7445),((3.5073, 4.8890), 27.3704), ((9.3900, 6.2406), 51.1350), ((8.7594, 6.7914), 50.5774), ((5.5016, 3.9552), 30.5206), ((6.2248, 3.6744), 31.7380), ((5.8704, 9.8798), 49.6374),((2.0774, 0.3774), 10.0634), ((3.0125, 8.8517), 38.0517),((4.7092, 9.1329), 43.5320), ((2.3049, 7.9618), 33.2198),((8.4431, 0.9871), 31.1220), ((1.9476, 2.6187), 16.2934),((2.2592, 3.3536), 19.3899), ((1.7071, 6.7973), 28.4807),((2.2766, 1.3655), 13.6945), ((4.3570, 7.2123), 36.9220),((3.1110, 1.0676), 14.9160), ((9.2338, 6.5376), 51.2371),((4.3021, 4.9417), 29.8112), ((1.8482, 7.7905), 32.0336),((9.0488, 7.1504), 52.5188), ((9.7975, 9.0372), 61.6658),((4.3887, 8.9092), 42.2733), ((1.1112, 3.3416), 16.5052),((2.5806, 6.9875), 31.3369), ((4.0872, 1.9781), 19.9475),((5.9490, 0.3054), 20.4239), ((2.6221, 7.4407), 32.6062),((6.0284, 5.0002), 35.1676), ((7.1122, 4.7992), 38.2211),((2.2175, 9.0472), 36.4109), ((1.1742, 6.0987), 25.0108),((2.9668, 6.1767), 29.8861), ((3.1878, 8.5944), 37.9213),((4.2417, 8.0549), 38.8327), ((5.0786, 5.7672), 34.4707)}

d = dict(D)
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
jump = []
global x1_test
global theta
newvals = []

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

#ax.plot(newvals, values, y_train, 'r')
ax.scatter(x_train, x2_train, y_train)

def cost_compute(x1_test):
	#print(x1_test)
	theta = np.ones(x1_test.shape)
	#print(y_test)
	hypothesis = theta.T * x1_test
	return hypothesis



def gradient_descent(x_test, y_train):
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
			cost = cost_compute(x1_test)
			print(myval)
			p = np.poly1d(x1_test)
			val = p(myval)
			values.append(val)
			newvals.append(myval)
			jump.append(cost)
		elif(k == 2):
			x1_test = np.array([1, x_train[i], x2_train[j], (x_train[i] ** 2), (x2_train[j] ** 2), (x_train[i] * x2_train[j])])
			#print(x_test)
			myval = gradient_descent(x1_test, y_train)
			cost = cost_compute(x1_test)
			p = np.poly1d(x1_test)
			val = p(myval)
			values.append(val)
			newvals.append(myval)
			jump.append(cost)
		elif(k == 3):
			x1_test = np.array([1, x_train[i], x2_train[j], (x_train[i] ** 3),(x2_train[j]**3),((x_train[j] ** 2) * x2_train[j]), (x_train[i] * (x2_train[j] ** 2))])
			myval = gradient_descent(x1_test, y_train)
			p = np.poly1d(x1_test)
			cost = cost_compute(x1_test)
			val = p(myval)
			values.append(val)
			jump.append(cost)
			newvals.append(myval)
		else:
			quit()


print(values)
#ax.scatter(x_train, x2_train, y_train, 'x')
#ax.plot(values, newvals, x1_test, 'r')
ax.plot(x_train, x2_train, y_train,'r')

ax.set_xlabel('x1')  
ax.set_ylabel('x2')
ax.set_zlabel('y')  
ax.set_title('') 
plt.show()

	








		
