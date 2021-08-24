#Ameet Subedi
#1001530023

from math import sqrt
from collections import Counter
import numpy as np
import sys
from statistics import mode

def get_class(dist,train,k):
	count = 0
	list1 = []
	
	list2 = []
	for e in dist:
		if count < k:
			list1.append(e)
			count += 1
	for x in list1:
		list2.append(train[x][train.shape[1]-1])

	data = Counter(list2[:])
	list1.clear()
	list2.clear()
	return(data.most_common())
	
	


def euclidean_distance(test,train):
	
	dist_list = []
	dis = {}
	for i in range(0,train.shape[0]):
		dist = 0
		for j in range(0,train.shape[1]):
			dist += np.power((test[j] - train[i][j]),2)
		dis[i] = sqrt(dist)
	return dis


out = np.loadtxt(sys.argv[1])
new_out = [i[:-1] for i in out]
new_out = np.array(new_out)
means = np.mean(new_out, axis = 0)
stds = np.std(new_out,axis = 0,ddof = 1)

for n,i in enumerate(stds):
	if i == 0:
		stds[n] = 1
dim = new_out.shape


for i in range(0,dim[0]):
	for j in range(0,dim[1]):
		new_out[i][j] = (new_out[i][j] - means[j])/stds[j]




test = np.loadtxt(sys.argv[2])
new_test = [i[:-1] for i in test]
new_test = np.array(new_test)
dim_test = new_test.shape
k = int(sys.argv[3])

for i in range(0,dim_test[0]):
	for j in range(0,dim_test[1]):
		new_test[i][j] = (new_test[i][j] - means[j])/stds[j]

distance = {}
count = 0
for i in range(0,dim_test[0]):
	distance = euclidean_distance(new_test[i],new_out)
	
	dist = {k: v for k, v in sorted(distance.items(), key=lambda item: item[1])}

	tu = get_class(dist,out,k)

	
	maxi = tu[0][1]
	l = []
	l.append(tu[0])
	for ams in range(1,len(tu)):
		if maxi == tu[ams][1]:
			l.append(tu[ams])
	
	if len(l) == 1:
			
		if l[0][0] == test[i][test.shape[1]-1 ]:
			acc = 1
			count += acc
		else:
			acc = 0
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%l[0][0] +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
	elif len(l) == 2:
		if l[0][0] == test[i][test.shape[1]-1 ] or l[1][0] == test[i][test.shape[1]-1 ]:
			acc = 1/2
			count += acc
		else:
			acc = 0
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%l[0][0] +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
	elif len(l) == 3:
		if l[0][0] == test[i][test.shape[1]-1 ] or l[1][0] == test[i][test.shape[1]-1 ] or  l[2][0] == test[i][test.shape[1]-1 ]:
			acc = 1/3
			count += acc
		else:
			acc = 0
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%l[0][0] +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
		
	else:
		acc = 1
		count += acc
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%l[0][0] +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
	
	l.clear()
print('classification accuracy=%6.4f\n' %(count/i))





	
	
	
