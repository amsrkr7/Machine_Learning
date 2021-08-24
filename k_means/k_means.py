#Ameet Subedi
#1001530023

from math import sqrt
import numpy as np
import sys
import random


def assign_clusters(data, k, initialization):
	dim = data.shape
	cluster = [[] for i in range(k)]
	counter = 0
	if initialization == 'round_robin':
		for i in range(0,dim[0]):
			cluster[counter].append(np.array(data[i]))
			counter += 1
			if counter == k:
				counter = 0

	if initialization == 'random':
		
		for i in range(0,dim[0]):
			counter = random.randint(0,k-1)
			cluster[counter].append(data[i])
	
	if len(dim) == 2:
		means = mean_calculation_2D(cluster)
		for i in range(k):
			for j in range(len(cluster[i])):
				cluster[i][j] = list(cluster[i][j])
		
	
	else:
		means = mean_calculation(cluster)
	lis = []
	lis.append(cluster)
	lis.append(means)	
	return lis	

def mean_calculation_2D(cluster):
	means = [[0 for i in range(2)] for j in range(k)]
	
	for i in range(k):
		sum1 = 0
		sum2 = 0
		for j in range(len(cluster[i])):
			sum1 += cluster[i][j][0]
			sum2 += cluster[i][j][1]
		if len(cluster[i]) == 0:
			means[i][0] = 0
			means[i][1] = 0
		else:
			
			means[i][0] = sum1/len(cluster[i])
			means[i][1] = sum2/len(cluster[i])
	for i in range(len(means)):
		means[i] = list(means[i])
	
	return means


def mean_calculation(cluster):
	means = [0 for i in range(len(cluster))] 
	for i in range(len(cluster)):
		if len(cluster[i]) == 0:
			means[i] = 0
		else:
			means[i] = sum(cluster[i])/len(cluster[i])
	return means



def euclidean_distance(x,y):
	dist = 0

	if l == 1:
		dist = np.power(x - y,2)
	else:
		for i in range(len(x)):
			dist += np.power(x[i] - y[i],2)
	return sqrt(dist)

def Classify(means,item):
	mini = 100000
	ind = -1

	for i in range(0,len(means)):
		dist = euclidean_distance(item,means[i])

		if (dist < mini):
			mini = dist
			ind = i
	return ind


def Fostering(data,cluster,means,belongs,k,l,maxI = 100000):
	selongs = belongs[:]
	

	for ams in range(maxI):
		

		for i in range(len(data)):
			item = data[i]
			index = Classify(means,item)

			if (belongs[i] != index):

				
				cluster[belongs[i]].remove(item)
				cluster[index].append(item)
				belongs[i] = index


		if l == 1:

			means = mean_calculation(cluster)
		else:
			means = mean_calculation_2D(cluster)
				

				

		if belongs == selongs:
			
			break
		selongs = belongs[:]
	
	return belongs



out = np.loadtxt(sys.argv[1])
dimension = out.shape
l = len(dimension)

k = int(sys.argv[2])
initialization = sys.argv[3]


if l == 2:
	data = []

	for i in range(len(out)):
		data.append(list(out[i]))



lis = assign_clusters(out, k, initialization)
cluster = lis[0]
ini_means = lis[1]




belongs = [-1 for i in range(len(out))]

for i in range(len(out)):
	for j in range(len(cluster)):
		if l == 1:
			if out[i] in cluster[j]:
				belongs[i] = j
				break
		else:
			
			
			
			if data[i] in cluster[j]:
				belongs[i] = j
				break
if l == 2:
	content = Fostering(data,cluster,ini_means,belongs,k,l)
else:

	content = Fostering(out,cluster,ini_means,belongs,k,l)



#contains = Clustering(out,ini_means,k,l)

if l == 2:
	for i in range(len(out)):
		print("("+"%10.4f,"%out[i][0] +" %10.4f"%out[i][1] + ") -->" +" cluster %d" %(content[i]+1))
else:
	for i in range(len(out)):
		print("%10.4f" %out[i] + " --> " + "cluster %d"%(content[i]+1))



#print(out[1])

#print(len(dimension))