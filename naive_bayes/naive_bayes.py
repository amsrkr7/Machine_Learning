#Ameet Subedi
#1001530023
import math
import numpy as np
import sys

def print_elsewhere(lol,i,test,round_precision):
	if (len(lol) == 1 and (lol[0]+1) == test[i][len(test[0]) - 1]):
		acc = 1.00
		print("ID=%5d,"%(i+1) +" predicted=%3d,"% (lol[0]+1) +"probability = %.4f,"%max(round_precision) + "true=%3d,"% test[i][len(test[0])- 1]+"accuracy=%4.2f\n"%acc)
		return acc
	elif (len(lol) == 1 and (lol[0]+1) != test[i][len(test[0]) - 1]):
		acc = 0.00
		print("ID=%5d,"%(i+1) +" predicted=%3d,"% (lol[0]+1) +"probability = %.4f,"%max(round_precision) + "true=%3d,"% test[i][len(test[0])- 1]+"accuracy=%4.2f\n"%acc)
		return acc
	elif(len(lol) > 1 and check(lol,test[i][len(test[0]) -1])):
		acc = 1/len(lol)
		print("ID=%5d,"%(i+1) +" predicted=%3d,"% (lol[0]+1) +"probability = %.4f,"%max(round_precision) + "true=%3d,"% test[i][len(test[0])- 1]+"accuracy=%4.2f\n"%acc)
		return acc
	elif (len(lol) > 1 and check(lol,test[i][len(test[0]) -1])):
		acc = 0
		print("ID=%5d,"%(i+1) +" predicted=%3d,"% (lol[0]+1) +"probability = %.4f,"%max(round_precision) + "true=%3d,"% test[i][len(test[0])- 1]+"accuracy=%4.2f\n"%acc)
		return acc

	return 0

def check(lol,num):
	lol = set(lol)
	if num in lol:
		return 1
	else:
		return 0


def mean_sd(classes, num):
	dim = classes.shape
	data = []
	mean = []
	meanSD = []
	summary = []
	SD = []
	gaussian =[]
	for j in range(0,dim[1]-1):
		for i in range(0,dim[0]):
			data.append(classes[i][j])
		avg = sum(data)/ len(data)
		add = 0
		for k in data:
			add = add + ((k - avg)*(k - avg))
		#print(add,len(data))
		stdev = np.std(data)
		if (stdev < 0.01):
			stdev = 0.01
		data.clear()
		print("Class %d, " %num + "Attribute %d, " %(j+1) + "mean = %.2f, " %avg + "sd %.2f"%stdev)

		mean.append(avg)
		SD.append(stdev)
		meanSD = merge(mean,SD)
	return(meanSD)


def merge(list1, list2): 
      
    merged_list = tuple(zip(list1, list2))  
    return merged_list 
      

#val = input("Enter a pathname: ")
out = np.loadtxt(sys.argv[1])

dimension = out.shape

new_out = [out[out[:,dimension[1]-1] == k] for k in np.unique(out[:,dimension[1] -1])]


count = 0


acc = []
prob_classes = []
for i in range(0,len(new_out)):
	for j in range(0,len(new_out[i])):
		count += 1
	prob = count/dimension[0]
	count = 0
	prob_classes.append(prob)
Lis =[]
for i in range(0,len(new_out)):
	results = mean_sd(new_out[i], i + 1)
	l = list(results)
	Lis.append(l)


#enter = input("Enter a test file: ")
test = np.loadtxt(sys.argv[2])
arr = test.shape
gaussian_X = 1;
arko = []

naive = []
Class_given_X = []

for i in range(0,arr[0]):
	for k in range(0,len(new_out)):
		l = 0
		for j in range(0,arr[1] - 1):
			expo = (pow((test[i][j] - Lis[k][l][0]),2))/(pow((Lis[k][l][1]),2))*(-1)
			e = np.exp(expo)
			numerical = 1/((Lis[k][l][1] * math.sqrt(2*np.pi)))
			gauss = numerical * e
			gaussian_X = gaussian_X * gauss 
			l = l+1
		
		arko.append(gaussian_X)
		gaussian_X = 1

	sum_rule = 0
	for x in range(0,len(new_out)):	
		sum_rule = sum_rule + (arko[x] * prob_classes[x])
	for q in range(0,len(new_out)):
		C_given_X = (arko[q]*prob_classes[q])/sum_rule
		Class_given_X.append(C_given_X)
	round_precision = [round(num,4) for num in Class_given_X]
	
	naive = max(round_precision)
	lol = [u for u,v in enumerate(round_precision) if v == naive]
	tot = print_elsewhere(lol,i,test,round_precision)
	acc.append(tot)
	
	Class_given_X.clear()
	arko.clear()
class_acc = sum(acc)/len(acc)
print("classification accuracy = %6.4f"%class_acc)

