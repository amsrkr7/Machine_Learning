#Ameet Subedi
#1001530023

import numpy as np
import random
import sys
import csv



def Utility(U,r,c,env):

	lis = []
	actionChoice = ["up" , "down", "left", "right"]
	for action in actionChoice:
		sum = 0
		if action == "up":

			
			if r == 0:

				if c == 0:
					if env[r][c+1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c] + 0.1 * U[r][c+1])
					else:
						sum = (0.8 * U[r][c]+0.1 * U[r][c] + 0.1 * U[r][c])

				elif c != 0 and c != (len(U[r]) -1):
					if env[r][c+1] != 'X' and env[r][c-1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c]+0.1 * U[r][c+1])
					if env[r][c+1] == 'x':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])

				elif c == (len(U[r]) - 1):
					if env[r][c-1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					else:
						sum = (0.8 * U[r][c]+0.1 * U[r][c]+0.1 * U[r][c])

				p = r
				q = c

			if r != 0:

				if c == 0:
					if env[r-1][c] != 'X'  and env[r][c+1] != 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c] + 0.1 * U[r][c+1])
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c]+0.1 * U[r][c+1])
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c]+0.1 * U[r][c])

				elif c != 0 and c != (len(U[r]) -1):
					if env[r-1][c] != 'X' and env[r][c-1] != 'X' and env[r][c+1] != 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c]+0.1 * U[r][c+1])

					if env[r][c+1] == 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c-1]+0.1 * U[r][c])

				elif c == (len(U[r]) - 1):
					if env[r-1][c] != 'X' and env[r][c-1] != 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r-1][c]+0.1 * U[r][c]+0.1 * U[r][c])

				p = r - 1
				q = c

			lis.append(sum)

			

		elif action == "down":


			if r == U.shape[0] - 1:

				if c == 0:
					if env[r][c+1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c] + 0.1 * U[r][c+1])
					else:
						sum = (0.8 * U[r][c]+0.1 * U[r][c] + 0.1 * U[r][c])


				elif c != 0 and c != (len(U[r]) -1):
					if env[r][c-1] != 'X'  and env[r][c+1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c]+0.1 * U[r][c+1])
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])


				elif c == (len(U[r]) - 1):
					if env[r][c-1] != 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					else:
						sum = (0.8 * U[r][c]+0.1 * U[r][c]+0.1 * U[r][c])


				p = r
				q = c

			if r != U.shape[0] - 1:

				if c == 0:
					if env[r+1][c] != 'X'  and env[r][c+1] != 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c] + 0.1 * U[r][c+1])
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c] + 0.1 * U[r][c+1])
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c] + 0.1 * U[r][c])


				elif c != 0 and c != (len(U[r]) -1):
					if env[r+1][c] != 'X' and  env[r][c-1] == 'X'  and env[r][c+1] == 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c+1])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c]+0.1 * U[r][c+1])
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c-1]+0.1 * U[r][c])


				elif c == (len(U[r]) - 1):
					if env[r+1][c] != 'X'  and env[r][c-1] != 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c]+0.1 * U[r][c-1]+0.1 * U[r][c])
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r+1][c]+0.1 * U[r][c]+0.1 * U[r][c])


				p = r + 1
				q = c
		
			lis.append(sum)

			

		elif action == "left":
			if c == 0:

				if r == 0:
					if env[r+1][c] != 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					else:
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r][c] )


				elif r !=0 and r != (U.shape[0] -1):
					if env[r+1][c] != 'X' and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c]+ 0.1 * U[r-1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c]+ 0.1 * U[r-1][c] )
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c]+ 0.1 * U[r][c] )

				elif r == U.shape[0] -1:
					if env[r-1][c] != 'X':
						sum = (0.8 * U[r][c] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					else:
						sum = (0.8 * U[r][c] + 0.1*U[r][c] + 0.1 * U[r][c] )

				p = r
				q = c

			if c != 0:

				if r == 0:
					if env[r][c-1] != 'X' and env[r+1][c] != 'X':
						sum = (0.8 * U[r][c-1] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c-1] + 0.1 * U[r][c] + 0.1 * U[r][c] )


				elif r !=0 and r != (U.shape[0] -1):

					if env[r][c-1] != 'X'  and env[r+1][c] != 'X' and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c-1] + 0.1 * U[r+1][c]+ 0.1 * U[r-1][c] )
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c]+ 0.1 * U[r-1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c-1] + 0.1 * U[r][c]+ 0.1 * U[r-1][c] )
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c-1] + 0.1 * U[r+1][c]+ 0.1 * U[r][c] )
						



				elif r == (U.shape[0] -1):
					if env[r][c-1] != 'X'  and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c-1] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					if env[r][c-1] == 'X':
						sum = (0.8 * U[r][c] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c-1] + 0.1*U[r][c] + 0.1 * U[r][c] )


				p = r
				q = c - 1
			lis.append(sum)

			

		elif action == "right":
			if c == U.shape[1] - 1:

				if r == 0:
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					else:
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r][c] )


				elif r !=0 and r != U.shape[0] -1:
					if env[r+1] != 'X'  and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c]+ 0.1 * U[r-1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c]+ 0.1 * U[r-1][c] )
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c]+ 0.1 * U[r][c] )


				elif r == U.shape[0] -1:
					if env[r-1][c] != 'X':
						sum = (0.8 * U[r][c] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					else:
						sum = (0.8 * U[r][c] + 0.1*U[r][c] + 0.1 * U[r][c] )

				p = r
				q = c

			if c != U.shape[1] - 1:

				if r == 0:
					if env[r][c+1] != 'X'  and env[r+1][c]  != 'X':
						sum = (0.8 * U[r][c+1] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r][c] + 0.1 * U[r+1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c+1] + 0.1 * U[r][c] + 0.1 * U[r][c] )


				elif r !=0 and r != U.shape[0] -1:
					if env[r][c+1] != 'X' and env[r+1][c] != 'X'  and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c+1] + 0.1 * U[r+1][c]+ 0.1 * U[r-1][c] )
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r][c] + 0.1 * U[r+1][c] + 0.1 * U[r-1][c] )
					if env[r+1][c] == 'X':
						sum = (0.8 * U[r][c+1] + 0.1 * U[r][c] + 0.1 * U[r-1][c] )
					if env[r-1][c] == 'X':
						sum = (0.8 * U[r][c+1] + 0.1 * U[r+1][c]+ 0.1 * U[r][c] )

				elif r == U.shape[0] -1:
					if env[r][c+1] != 'X' and env[r-1][c] != 'X':
						sum = (0.8 * U[r][c+1] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					if env[r][c+1] == 'X':
						sum = (0.8 * U[r][c] + 0.1*U[r-1][c] + 0.1 * U[r][c] )
					if env[r-1][c] =='X':
						sum = (0.8 * U[r][c+1] + 0.1*U[r][c] + 0.1 * U[r][c] )

				p = r
				q = c+1

			lis.append(sum)
			
	
	this = lis[:]
	lis.clear()
	return this
	




with open(sys.argv[1]) as inFile:
	env = list(csv.reader(inFile))


U_prime = np.zeros([len(env), len(env[0])])

R = np.zeros([len(env), len(env[0])])

reward = float(sys.argv[2])

gamma = float(sys.argv[3])

K = int(sys.argv[4])

for i in range(len(env)):
	for j in range(len(env[0])):
		if env[i][j]== '.':
			R[i][j] = reward
		elif env[i][j] == 'X':
			R[i][j] == 0
		elif env[i][j] == '-1.0':
			R[i][j] = -1
		else:
			R[i][j] = 1


for i in range(K):
	U = U_prime.copy ()

	for r in range(len(env)):
		for c in range(len(env[0])):

			if (U[r][c] == 1.0) or (U[r][c] == -1.0):
				U_prime[r][c] = U[r][c]
			elif (R[r][c] == 0):
				U_prime[r][c] = 0
			else:
				summation = Utility(U,r,c,env)
				
				U_prime[r][c] =  R[r][c] + (gamma * (max(summation)))
print('\n\n')

print("utilities:")
for i in range(len(env)):
	for j in range(len(env[0])):
		print ('{:6.3f}'.format(U_prime[i][j]),end = " ")
	print('\n')

print('\n')

actions = ["up","down","left","right"]

Optimal = [['x' for i in range(len(env[0]))] for j in range(len(env))]





for i in range(len(env)):
	for j in range(len(env[0])):

		if (U_prime[i][j] == 1.0) or (U_prime[i][j] == -1.0):
			Optimal[i][j] = 'o'
		elif (U_prime[i][j] == 0):
			Optimal[i][j] = 'x'
		else:
			avg = Utility(U_prime,i,j,env)
			maxi = max(avg)
			ind = avg.index(maxi)
			if ind == 0:
				Optimal[i][j] = '^'
			elif ind == 1:
				Optimal[i][j] = 'v'
			elif ind == 2:
				Optimal[i][j] = '<'
			elif ind == 3:
				Optimal[i][j] = '>'

print("policy:")
for i in range(len(env)):
	for j in range(len(env[0])):
		print ('{:6s}'.format(Optimal[i][j]),end = " ")
	print('\n')
	




