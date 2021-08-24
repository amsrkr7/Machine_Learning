#Ameet Subedi
#1001530023
import math
import numpy as np 
import random
import sys

def network(w,b,file,ams):

	dim = file.shape
	z = []
	yeti = []
	for j in range(0,dim[1]):
		yeti.append(file[ams][j])
	z.append(yeti[:])
		
	yeti.clear()

	a = []
	act_func = []
	a.append(0)
	som = []
	f = np.empty((J,J))
	g = np.empty((nb_classes, J))
	for l in range(1,L - 1):
		for i in range(0,J):
			prod = 0
			for j in range(0,len(z[l-1])): 
				prod = prod +(w[l][i][j] * z[l-1][j])
			prod = b[l][i] + prod
			som.append(prod)
			act_func.append(1/(1+np.exp(prod)))
		a.append(som[:])
		z.append(act_func[:])
		act_func.clear()
		som.clear()


	for i in range(0,nb_classes):
		prod = 0
		for j in range(0,len(z[L - 2])):
			prod = prod + (w[L-1][i][j] * z[L - 2][j])
		prod = b[L-1][i] + prod
		som.append(prod)
		act_func.append(1/(1+np.exp(prod)))
	a.append(som[:])
	z.append(act_func[:])
	som.clear()
	act_func.clear()
	return z



out = np.loadtxt(sys.argv[1])
class_label = out[:,-1]
nb_classes = (max(class_label)).astype(int)
targets = (np.array(class_label).reshape(-1)).astype(int) - 1
one_hot_targets = np.eye(nb_classes)[targets]



new_out = [i[:-1] for i in out]
new_out = np.array(new_out)

test = np.loadtxt(sys.argv[2]) 
c_label = test[:,-1]
test = [j[:-1] for j in test]


max = np.amax(new_out)
new_out = new_out/max
dim = new_out.shape
test = test/max

dimension = test.shape

L = int(sys.argv[3])
J = int(sys.argv[4])
round = int(sys.argv[5])
w = [[]]*(L)
w[0] = 0

rand_w,rand_b, rand_b_last = [],[],[]
b = [[]]*(L)
b[0] = [0]
for i in range(1,L - 1):
	for j in range(0,J):
		rand_b.append(np.random.uniform(-0.05,0.05))
	b[i] = rand_b[:]
	rand_b.clear()
for i in range(0,nb_classes):
	rand_b_last.append(np.random.uniform(-0.05,0.05))
b[L-1] = rand_b_last


for i in range(0,dim[1]):
	rand_w.append(np.random.uniform(-0.05,0.05))

k = np.zeros((J,dim[1]))
for i in range(0,J):
	for j in range(0,dim[1]):
		k[i][j] = rand_w[j]

w[1] = k

rand_w.clear()

for i in range(0,J):
	rand_w.append(np.random.uniform(-0.05,0.05))
p = np.zeros((J,J))
for c in range(0,J):
	for d in range(0,J):
		p[c][d] = rand_w[d]
w[2] = p
rand_w.clear()
for i in range(0,J):
	rand_w.append(np.random.uniform(-0.05,0.05))

g = np.zeros((nb_classes,J))
for c in range(0,nb_classes):
	for d in range(0,J):
		g[c][d] = rand_w[d]
w[L-1] = g
l = np.zeros((J,J))
for i in range(2,L-1):	
	w[i] = k

rand_w.clear()


z_output = []
for r in range(1,round+1):
	for ams in range(0,dim[0]):
		z_output = network(w,b,new_out,ams)
		count = 0;
		delta = [[]]*L
		secondary = []
		tertiary = []
		for i in range(0,nb_classes):
			secondary.append((z_output[L-1][i] - one_hot_targets[ams][i])*z_output[L-1][i]*(1-z_output[L-1][i])) 
		delta[L-1] = secondary
		for l in range(L-2,0,-1):
			for i in range(0,J):
				prod = 0
				for k in range(0,len(z_output[l+1])):
					prod = prod + (delta[l+1][k]*w[l+1][k][i])
				tertiary.append(prod * z_output[l][i]*(1 - z_output[l][i]))
			delta[l] = tertiary[:]
			tertiary.clear()

		for l in range(1,L-1):
			for i in range(0,J):
				b[l][i] = b[l][i] -(pow(0.98,r-1) * delta[l][i])
				for j in range(0,len(z_output[l -1])):
					w[l][i][j] = w[l][i][j] - (pow(0.98,r-1) * delta[l][i]*z_output[l-1][j]) 

		for i in range(0,nb_classes):
			b[L-1][i] = b[L-1][i] - (pow(0.98,r-1) * delta[L-1][i])
			for j in range(0,len(z_output[L - 2])):
				w[L-1][i][j] = w[L-1][i][j] - (pow(0.98,r-1) * delta[L - 1][i]*z_output[L-2][j])



for ams in range(0,dimension[0]):
	g = network(w,b,test,ams)
	last = g[len(g)-1]
	result = np.where(last == np.amax(last))
	count = 0
	if (result[0][0] == c_label[ams]):
		acc = 1
		count +=1
	else:
		acc = 0
	print("ID=%5d,"%(ams+1) +" predicted=%3d,"%result[0][0] +"true = %.4f,"%c_label[ams] + "accuracy=%4.2f\n"%acc)


print("classification accuracy = %6.4f"%(count/ams))
