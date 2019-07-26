#import sys
import numpy as np
import pandas as pd
import random
from math import exp
import csv

dataset = []

value_list = []

def make_predictions(r, theta):
	op = theta[1]
	ex = 0
	print(len(r))
	try:
		for mk in range(len(r)-1):
			#print(j)
			print(theta, op, mk)
			op += (theta[mk] * r[mk])
		return 1 / (1 + exp(-op))
	except:
		print("Done")
		exit()

def gradient_descent(myset, lRate, n):
	c = []
	for l in range(len(myset[0])):
		c.append(0)

	for p in range(n):
		err = 0
		try:
			for kv in myset:
				op = make_predictions(kv, c)
				err = kv[-1] - op
				err = err + err ** 2
				c[0] = c[0] + lRate * err * op * (1.0 - op)
				for jk in range(0, len(kv)-1):
					#incr = jk
					c[jk] = c[jk] + alpha * err * op * (1.0 - op) * kv[jk]
		except:
			print("done")
			exit()
	return c

def get_training_set(mylist, the_set):
	with open('mydata.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		lis = list(readCSV)
		for i in range(len(lis)):
			for j in range(len(lis[i])):
				if(lis[i][j] == 'W'):
					lis[i][j] = 0
				elif(lis[i][j] == 'M'):
					lis[i][j] = 1
				lis[i][j] = int(lis[i][j])
			value_list.append(lis[i])
		return value_list

train_set = []
mydataset = get_training_set('mydata.csv', train_set)
epch_num = 50
alpha = 0.01
theta_value = gradient_descent(mydataset, alpha, epch_num)
print("Theta values for gradient descent are: ", theta_value)
test_set_list = []
initialize = []

test_set = get_training_set('test_one.csv', test_set_list)
test_set_two = get_training_set('test_two.csv', initialize)

take = []
for tk in range(0, len(test_set_two)):
	take.append(test_set_two[tk][-1])

for kn in test_set_two:
	del kn[-1]

print("the test set is: ", test_set_two)

while(len(test_set)!=0):
	women_class = []
	men_class = []
	predict_gender = []
	for link in test_set:
		op = make_predictions(link, theta_value)
		if(int(round(op)) == 0):
			g_p = 0
			predict_gender.append(g_p)
		if(int(round(op)) == 1):
			g_p = 1
			predict_gender.append(g_p)
		women_class_min = op - 0
		women_class.append(women_class_min)
		men_class_min = 1 - op
		men_class.append(men_class_min)
	print("The predictions are : ", predict_gender)

	total_minimum_li = []
	for iterate in range(0,len(women_class)):
		total_element=min(women_class[iterate],men_class[iterate])
		total_minimum_li.append(total_element)

	element_min_index = total_minimum_li.index(min(total_minimum_li))
	test_set[element_min_index].append(predict_gender[element_min_index])
	mydataset.append(test_set[element_min_index])
	del test_set[element_min_index]
	print("Length of unlabeled data is: ", len(test_set))

	Theta = gradient_descent(mydataset, alpha, epch_num)
	print(Theta)

predicted_answer = []
for count in range(len(test_set_two)):
	op1 = make_predictions(test_set_two[count], Theta)
	if(int(round(op1)) == 0):
		gender = "Woman"
		print("Number: {} Prediction: {}".format(test_set_two[count], gender))
		rounded = int(round(op1))
		predicted_answer.append(rounded)
	elif(int(round(op1)) == 1):
		gender = "Man"
		print("Number: {} Prediction: {}".format(test_set_two[count], gender))
		rounded = int(round(op1))
		predicted_answer.append(rounded)
	else:
		print("No such gender or person")
	print(predicted_answer)

	acc_count = 0

	for kb in range(0, len(take)):
		if(predicted_answer[kb] == take[kb]):
			acc_count = acc_count + 1

		

	print(acc_count)

	Accuracy = (acc_count/len(take)) * 100
	print("The accuracy for the model is: ", Accuracy)




           