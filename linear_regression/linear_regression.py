#Ameet Subedi
#1001530023

import math
import numpy as np
import sys


def phi(matrix,deg):
	arr = []
	mat = []
	dat = []
	for i in range(0,matrix.shape[0]):
		arr.append(1)
		for j in range(1,matrix.shape[1]):
			for k in range(1,deg+1):
				arr.append(pow(matrix[i][j],k))
		mat.append(arr)
		arr = []
	mat = np.array(mat)
	return mat



out = np.loadtxt(sys.argv[1])
dimension = out.shape
#print(dimension)

new_out = [i[:-1] for i in out]
new_out = np.array(new_out)
dim = new_out.shape


new_out = np.insert(new_out,0,1,axis = 1)
phi_matrix= phi(new_out,int(sys.argv[3]))


phi_transpose = np.transpose(phi_matrix)

t = out[:,dimension[1] -1]

t = np.asmatrix(t)
t = np.transpose(t)


phi_dot = np.dot(phi_transpose,phi_matrix)

identity = np.identity(phi_dot.shape[0])
lambda_identity = int(sys.argv[4]) *identity
first_exp = np.add(lambda_identity,phi_dot)
first_exp_pinv = np.linalg.pinv(first_exp)

transpose_t = np.dot(phi_transpose,t)
w = np.dot(first_exp_pinv,transpose_t)

for i in range(0,w.shape[0]):
	
	print("w%d"  %i + "= %.4f" %w[i])

test = np.loadtxt(sys.argv[2])
new_test = [i[:-1] for i in test]
new_test = np.array(new_test)
new_test = np.insert(new_test,0,1,axis = 1)
test_matrix = phi(new_test,int(sys.argv[3]))

test_matrix_transpose = np.transpose(test_matrix)

for i in range(0,test_matrix.shape[0]):
	test_row = test_matrix[i,:]
	test_column = np.transpose(np.asmatrix(test_row))
	output = np.dot(np.transpose(w),test_column)
	print("ID=%5d,"%(i+1) + "output=%14.4f,"%output[0][0] + "target value = %10.4f,"%test[i][test.shape[1]-1]+"squared error = %.4f" %pow((output[0][0] - test[i][test.shape[1]-1]),2))



