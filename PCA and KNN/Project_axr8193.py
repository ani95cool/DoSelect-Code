import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter





df = pd.read_csv('heart.csv')



t = df.copy()
col_names = []
s = t.iloc[:, : -1]
features = t['target']
f = list(features)
new_features = []
for le in range(len(features)):
    if(features[le] == 1):
        new_features.append('Y')
    elif(features[le] == 0):
        new_features.append('N')
    else:
        print("No such label available")
t.loc[:, 'target'].replace(f, new_features, inplace=True)
for keys in t.columns:
    col_names.append(keys) 

u = []
mean_vector = np.mean(s, axis=0)
dic = dict(mean_vector)
k = dic.values()
lis = [vals for vals in k]
#lis
my_list = np.array(lis)

a = []
l = []
#s = df.copy()
dic = {}
#my_list = np.reshape(my_list, (my_list.shape[0], 1))
#print(l)
m = s.shape[1]
#print(np.cov(s.T))
val = []
#one_less = num - 1
#print(np.cov(s.T))
#print(s)    
for i,j in s.iterrows():
    val.append([j])
a.append(val)
#cov_mat = (nary - my_list).T.dot((nary - my_list)) / (nary.shape[0]-1)
cov_mat = np.cov(s.T)
#nary = np.array(a)
#cov_mat

new_li = [cols for cols in s.columns]
new_df = pd.DataFrame(cov_mat, columns=new_li)
print(new_df)

#new_df

eig_vals, eig_vecs = np.linalg.eig(np.array(cov_mat))


eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]


eig_pairs.sort(key=lambda x: x[0], reverse=True)

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
cum_var_exp.shape
new_var = list(cum_var_exp)

num_vectors = 0.0
exp_var_percentage = 0.97
pctage = float(exp_var_percentage * 100)

#print(len(new_var))
#print(new_var)
true_arr = []
false_arr = []
for id in range(0, len(new_var)):
    #print(pctage)
    if(float(pctage) < new_var[id]):
        true_arr.append(True)
    else:
        false_arr.append(False)
#len(true_arr)



num_vectors = len(true_arr)
num_features = s.shape[1]
proj_mat = eig_pairs[0][1].reshape(num_features,1)


for idx in range(1, num_vectors):
    proj_mat = np.hstack((proj_mat, eig_pairs[idx][1].reshape(num_features,1)))


pca_mat = np.dot(s, proj_mat) 
#pca_mat.shape


#col_names


new_li = []
for c in range(len(col_names)-3):
    new_li.append(col_names[c])


second_df = pd.DataFrame(pca_mat, columns=new_li)
#print(second_df)


second_df['target'] = t.target
print(second_df)


x = df.iloc[:, : -1]
y = df['target']
nl = []
new_y = second_df['target']
#print(len(new_y))
for mn in range(len(new_y)):
    nl.append(new_y[mn])



X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
print(X_test)


def euclideanDistance():
    #distance = 0
    #mli = []
    x_df = second_df.iloc[:, : -1]
    a_list = []
    distance = []
    for i,j in X_test.iterrows():
        a_list.append([j['age'], j['sex'], j['cp'], j['trestbps'], j['chol'], j['fbs'], j['restecg'], j['thalach'], j['exang'], j['oldpeak'], j['slope']])
    t = tuple(a_list)
    #print(t)
    mytup = ()
    kn = len(t)
    for j in range(kn):
        tup = tuple(t[j])
        for u,v in x_df.iterrows():
            mytup = [v['age'], v['sex'], v['cp'], v['trestbps'], v['chol'], v['fbs'], v['restecg'], v['thalach'], v['exang'], v['oldpeak'], v['slope']]
            for km in range(len(tup)):
                #print(tup[km])
                for ky in range(len(mytup)):
                    cartesian_distance = 0
                    for iy in range(len(nl)):
                        d_i = np.sqrt((mytup[ky] - tup[km]) ** 2)
                        cartesian_distance += d_i
                        l = [cartesian_distance, tup, nl[iy]]
                #rint(l)
            distance.append(l)
        return distance   
            #print(distance)

temp = '''
    distance=[]
    for j in range(kn):
        test_tup = tuple(t[j])
        #print("test_tup idx:"+str(j)+str(test_tup))
        for u,v in x_df.iterrows():
            train_tup = [v['age'], v['sex'], v['cp'], v['trestbps'], v['chol'], v['fbs'], v['restecg'], v['thalach'], v['exang'], v['oldpeak'], v['slope']]
            #print("train_tup idx:"+str(u)+str(train_tup))
            cartesian_distance = 0
            min_dist = np.zeros((len(distance),1))
            for km in range(len(test_tup)):
                d_i = np.sqrt((train_tup[km] - test_tup[km]) ** 2)
                cartesian_distance += d_i
            l = np.array([cartesian_distance, u])
            min_dist = np.vstack((min_dist, l))
    return min_dist
    '''
            
def k_nearest_neighbours(dataset, k):
    #vote = [o[2] for o in sorted(dataset)[0:k]]
    #print(dataset)
    for im in range(k):
        index = im + 1
        patient = "Patient " + str(index)
        if(dataset[2][2] == 'N'):
            print(patient, "doesnot have a heart disease!!")
        elif(dataset[2][2] == 'Y'):
            print(patient, "does have a heart disease!!")
        else:
            print("no such label")
    #print(vote)
    #vote_result = Counter(vote).most_common(1)[0][0]
    #print(vote_result)
    #print(vote)
    

op = euclideanDistance()
k = int(input("Enter the value of K: "))
k_nearest_neighbours(op, k)