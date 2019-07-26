
from collections import Counter

#dataset initialization
D = { ((170, 57, 32), 'W'),
((192, 95, 28), 'M'),
((150, 45, 30), 'W'),
((170, 65, 29), 'M'),
((175, 78, 35), 'M'),
((185, 90, 32), 'M'),
((170, 65, 28), 'W'),
((155, 48, 31), 'W'),
((160, 55, 30), 'W'),
((182, 80, 30), 'M'),
((175, 69, 28), 'W'),
((180, 80, 27), 'M'),
((160, 50, 31), 'W'),
((175, 72, 30), 'M')

}

features = (155, 40, 35)
dataset = tuple(D)
#print(dataset)



def k_nearest_neighbours(dataset, features, k=5):
	if(len(dataset) >= k):
		print("The value of K is less than the minimum")

	distance = []
	for i in range(len(dataset)):
		for j in range(len(dataset[i])):
			for k in range(len(dataset[i][0])):
				cartesian_distance = 0
				for h in range(len(features)):
					d_i = (dataset[i][0][k] - features[h])**2
					cartesian_distance += d_i
				cartesian_distance = cartesian_distance ** 0.5	
			    		
			l = [cartesian_distance, dataset[1][1]]

		distance.append(l)
	#print(distance)
	print(distance)
    
	vote = [i[1] for i in sorted(distance)[0:k+1]]
	print(vote)
	vote_result = Counter(vote).most_common(1)[0][0]
	print(vote_result)
	#vote_result = Counter(vote).most_common(1)[0][0]
	

	#print(cartesian_distance)		

	

k_nearest_neighbours(dataset, features, k=5)			

'''
d_i = (dataset[i][0][k] - features[h])**2
					cartesian_distance += d_i
					#cartesian_distance = sum(cartesian_distance ** 2)
'''