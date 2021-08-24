#Ameet Subedi
#1001530023

import math
import numpy as np
import sys
import random
from collections import Counter

sys.setrecursionlimit(2000)



class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self,best,examples,attributes,pruning_thr):
		examples_l = []
		examples_r = []
		for i in range(0,examples.shape[0]):
			if (examples[i][best[0]] < best[1]):
				examples_l.append(examples[i])
		else:
			examples_r.append(examples[i])

		examples_left = np.array(examples_l[:])
		examples_right = np.array(examples_r[:])
		examples_l.clear()
		examples_r.clear()
		self.left = DTL(examples_left,attributes, Distribution(examples),pruning_thr)
		self.right = DTL(examples_right,attributes,Distribution(examples),pruning_thr)

	

def TraverseTree(test,tree):
	x = isinstance(tree,Node)
	if not x: 
		return(tree)
		return a
	if  x:
		if test[tree.data[0]] < tree.data[1]:
			return TraverseTree(test,tree.left)
		elif test[tree.data[0]] >= tree.data[1]:
			return TraverseTree(test,tree.right)


def Distribution(examples):
	u_list = [0] * (len(x_label)+1)
	class_label = examples[:,-1]
	a = dict(Counter(class_label))
	for x in a:
		u_list[int(x)] = (a[x]/len(class_label))
	return u_list

def Select_Column(examples, A):
	attribute_values = []
	for i in range(0,examples.shape[0]):
		attribute_values.append(examples[i][A])
	return attribute_values


def DTL_TopLevel(examples,pruning_thr):
	dim = examples.shape
	new_out = [i[:-1] for i in examples]
	new_out = np.array(new_out)
	attributes = []
	for i in range(0,dim[1] - 1):
		attributes.append(i)
	default = Distribution(examples)
	return DTL(examples, attributes, default,pruning_thr)

def Information_gain(examples,A,threshold):
	less_than = []
	greater_than = []
	add = 0
	add_greater = 0
	add_less = 0
	
	for i in range(0,examples.shape[0]):
		if (examples[i][A] < threshold):
			less_than.append(examples[i])
		else:
			greater_than.append(examples[i])
	less_than_examples = np.array(less_than[:])
	greater_than_examples = np.array(greater_than[:])
	
	label = examples[:,-1]
	a = dict(Counter(label))
	example_class_occurence = [0] * (len(x_label)+1)
	less_than_class_occurence = [0] * (len(x_label)+1)
	greater_than_class_occurence = [0] * (len(x_label)+1)
	for x in a:
		example_class_occurence[int(x)] = a[x]

	if len(less_than) != 0:
		c_label_less_than = less_than_examples[:,-1]
		b = dict(Counter(c_label_less_than))
		 
		for x in b:	
			less_than_class_occurence[int(x)] = b[x]
	if len(greater_than)  != 0:
		c_label_greater_than = greater_than_examples[:,-1]
		c = dict(Counter(c_label_greater_than))
		 
		for x in c:
			greater_than_class_occurence[int(x)] = c[x]
	for i in range(0,int(max(x_label))):
		if example_class_occurence[i] != 0:
			add = add + ((example_class_occurence[i]/sum(example_class_occurence))*(np.log2(example_class_occurence[i]/sum(example_class_occurence))))

		if greater_than_class_occurence[i] != 0:
		 	add_greater = add_greater + ((greater_than_class_occurence[i]/sum(greater_than_class_occurence))*(np.log2(greater_than_class_occurence[i]/sum(greater_than_class_occurence))))

		if less_than_class_occurence[i] != 0:
			add_less = add_less + ((less_than_class_occurence[i]/sum(less_than_class_occurence))* (np.log2(less_than_class_occurence[i]/sum(less_than_class_occurence))))

	add = add * (-1)
	add_greater = add_greater * (-1)
	add_less = add_less *(-1)

	weight_less = sum(less_than_class_occurence)/sum(example_class_occurence)
	weight_greater = sum(greater_than_class_occurence)/sum(example_class_occurence)
	less_than.clear()
	greater_than.clear()
	less_than_class_occurence.clear()
	greater_than_class_occurence.clear()

	return add - (weight_less * add_less) - (weight_greater * add_greater)







def DTL(examples,attributes, default,pruning_thr):

	
	if examples.shape[0] < pruning_thr: return default
	if (sys.argv[3] == "optimized"):
		best = Choose_Attribute(examples,attributes)
	else:
		best = Choose_Attribute_Random(examples,attributes)
	tree = Node(best)

	tree.insert(best,examples,attributes,pruning_thr)


	return tree

def Choose_Attribute_Random(examples,attributes):
	best = [0]*2
	max_gain = best_threshold = -1
	A = random.choice(attributes)
	attribute_values = Select_Column(examples, A)
	L = min(attribute_values)
	M = max(attribute_values)


	for k in range(1,51):
		threshold = (((M-L)/51)*k)+L
		gain = Information_gain(examples,A,threshold)
		if gain > max_gain:
			max_gain = gain
			best[0] = A
			best[1] = threshold
	return(best)



def Choose_Attribute(examples,attributes):

	best = [0] * 2
	max_gain = best_attribute = best_threshold = -1
	for A in attributes:
		attribute_values = Select_Column(examples, A)
		L = min(attribute_values)
		M = max(attribute_values)


		for k in range(1,51):
			threshold = (((M-L)/51)*k)+L
			gain = Information_gain(examples,A,threshold)
			if gain > max_gain:
				max_gain = gain
				best[0] = A
				best[1] = threshold
	return(best)



out = np.loadtxt(sys.argv[1])
dimension = out.shape
out = np.array(out)
c_label = out[:,-1]
x_label = list(set(c_label))




pruning_thr = int(sys.argv[4])

dist = Distribution(out)

if (sys.argv[3] == "optimized" or sys.argv[3] == "randomized"):
	tree = DTL_TopLevel(out,pruning_thr)
elif (sys.argv[3] == "forest3"):
	forest3_1 = DTL_TopLevel(out,pruning_thr)
	forest3_2 = DTL_TopLevel(out,pruning_thr)
	forest3_3 = DTL_TopLevel(out,pruning_thr)
elif (sys.argv[3] == "forest15"):
	forest15_1 = DTL_TopLevel(out,pruning_thr)
	forest15_2 = DTL_TopLevel(out,pruning_thr)
	forest15_3 = DTL_TopLevel(out,pruning_thr)
	forest15_4 = DTL_TopLevel(out,pruning_thr)
	forest15_5 = DTL_TopLevel(out,pruning_thr)
	forest15_6 = DTL_TopLevel(out,pruning_thr)
	forest15_7 = DTL_TopLevel(out,pruning_thr)
	forest15_8 = DTL_TopLevel(out,pruning_thr)
	forest15_9 = DTL_TopLevel(out,pruning_thr)
	forest15_10 = DTL_TopLevel(out,pruning_thr)
	forest15_11 = DTL_TopLevel(out,pruning_thr)
	forest15_12 = DTL_TopLevel(out,pruning_thr)
	forest15_13 = DTL_TopLevel(out,pruning_thr)
	forest15_14 = DTL_TopLevel(out,pruning_thr)
	forest15_15 = DTL_TopLevel(out,pruning_thr)




test = np.loadtxt(sys.argv[2])
test = np.array(test)


if (sys.argv[3] == "optimized" or sys.argv[3] == "randomized"):

	count = 0
	counter = 0
	for i in range(0,test.shape[0]):
		counter += 1
		answer = TraverseTree(test[i],tree)
		if answer.index(max(answer)) == test[i][test.shape[1] - 1]:
			acc = 1
			count  = count + 1
		else:
			acc = 0
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%answer.index(max(answer)) +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
	print('classification accuracy=%6.4f\n' %(count/counter))

if (sys.argv[3] == "forest3"):
	count = 0
	counter = 0
	for i in range(0,test.shape[0]):
		counter += 1
		for_ans1 = TraverseTree(test[i],forest3_1)
		for_ans2 = TraverseTree(test[i],forest3_2)
		for_ans3 = TraverseTree(test[i],forest3_3)
		list1 = [(a+b+c)/3 for a,b,c in zip(for_ans1,for_ans2,for_ans3)]
		if list1.index(max(list1)) == test[i][test.shape[1] - 1]:
			acc = 1
			count  = count + 1
		else:
			acc = 0
		print('ID=%5d,'%(i+1) + 'predicted=%3d,'%list1.index(max(list1)) +' true=%3d,'%test[i][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)
	print('classification accuracy=%6.4f\n' %(count/counter))
if (sys.argv[3] == "forest15"):
	count = 0
	counter = 0
	for ams in range(0,test.shape[0]):
		counter += 1
		for1_ans1 = TraverseTree(test[ams],forest15_1)
		for1_ans2 = TraverseTree(test[ams],forest15_2)
		for1_ans3 = TraverseTree(test[ams],forest15_3)
		for1_ans4 = TraverseTree(test[ams],forest15_4)
		for1_ans5 = TraverseTree(test[ams],forest15_5)
		for1_ans6 = TraverseTree(test[ams],forest15_6)
		for1_ans7 = TraverseTree(test[ams],forest15_7)
		for1_ans8 = TraverseTree(test[ams],forest15_8)
		for1_ans9 = TraverseTree(test[ams],forest15_9)
		for1_ans10 = TraverseTree(test[ams],forest15_10)
		for1_ans11 = TraverseTree(test[ams],forest15_11)
		for1_ans12 = TraverseTree(test[ams],forest15_12)
		for1_ans13 = TraverseTree(test[ams],forest15_13)
		for1_ans14 = TraverseTree(test[ams],forest15_14)
		for1_ans15 = TraverseTree(test[ams],forest15_15)
		list2 = [(a+b+c+d+e+f+g+h+i+j+k+l+m+n+o)/15 for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o in zip(for1_ans1,for1_ans2,for1_ans3,for1_ans4,for1_ans5,for1_ans6,for1_ans7,for1_ans8,for1_ans9,for1_ans10,for1_ans11,for1_ans12,for1_ans13,for1_ans14,for1_ans15)]
		if list2.index(max(list2)) == test[ams][test.shape[1] - 1]:
			acc = 1
			count  = count + 1
		else:
			acc = 0
		print('ID=%5d,'%(ams+1) + 'predicted=%3d,'%list2.index(max(list2)) +' true=%3d,'%test[ams][test.shape[1]-1 ] +' accuracy=%4.2f\n' %acc)

	print('classification accuracy=%6.4f\n' %(count/counter))
		

