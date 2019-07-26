import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from matplotlib import style
from sklearn.model_selection import train_test_split

#style.use("ggplot")

x = []
li = []
y = []
z = []

D = { ((1, 2), (-1)),((2, 3), 1),((2, 1), (-1)),((3, 4), 1),((1, 3), (-1)),((4, 4), 1)}
name = ''
d = dict(D)
for k, v in d.items():
	li.append(k)
	z.append(v)





#loading the data into the dataframe
df = pd.DataFrame(li, columns = ['x', 'y'])
df.insert(2, 'z', value=z)

X1 = df['x']
X2 = df['y']

#k = int(input("Enter the order of your polynomial: "))

for sums in range(len(X1)):
	x.append(X1[sums])


for lines in range(len(X2)):
	y.append(X2[lines])




x_value = df.iloc[:, :-1]

X = np.array(x_value)
#print(X)


m = np.array(z)
Y = np.reshape(m, (3,2))

#print(Y)

#plt.scatter()
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(X1, X2)
plt.show()




model = SVC(kernel='linear', decision_function_shape='ovo')
clf = model.fit(X, m)
#model.score(X_test, Y_test)
p = clf.predict([[10.28, 10.23],[11.76, 11.54]])
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(0, 5)
yy = a * xx - clf.intercept_[0] / w[1]
b = clf.support_vectors_[1]
yy_below = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_top = a * xx + (b[1] - a * b[0])
h0 = plt.plot(xx, yy, 'k-',label="Decision Boundry")
h1 = plt.plot(xx, yy_below, 'k--',label="Lower Decision Boundry")
h2 = plt.plot(xx, yy_top, 'k--',label="Upper Decision Boundry")
#index1 = int(input("Which index of the matrix would : "))
plt.scatter(X1, X2, c=z)
plt.show() 
#support = clf.support_vectors_
