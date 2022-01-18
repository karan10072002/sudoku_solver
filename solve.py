# solving sudoku using backtracking

import numpy
# import os, time
#sudoko
# matrix=[[5,3,0,  0,7,0,  0,0,0],
#  [6,0,0,  1,9,5,  0,0,0],
#  [0,9,8,  0,0,0,  0,6,0],

#  [8,0,0,  0,6,0,  0,0,3],
#  [4,0,0,  8,0,3,  0,0,1],
#  [7,0,0,  0,2,0,  0,0,6],

#  [0,6,0,  0,0,0,  2,8,0],
#  [0,0,0,  4,1,9,  0,0,5],
#  [0,0,0,  0,8,0,  0,0,0]]

matrix=[[5,3,0,0,7,0,0,0,0],
	    [6,0,0,1,9,5,0,0,0],
	    [0,9,8,0,0,0,0,6,0],
	    [8,0,0,0,6,0,0,0,3],
	    [4,0,0,8,0,3,0,0,1],
	    [7,0,0,0,2,0,0,0,6],
	    [0,6,0,0,0,0,2,8,0],
	    [0,0,0,4,1,9,0,0,5],
	    [0,0,0,0,8,0,0,7,9]]


def present_in_grid(x,y,num):
	global matrix
	u=(x//3)*3
	v=(y//3)*3
	for i in range(3):
		for j in range(3):
			if matrix[v+i][u+j]==num:
				return True
	return False

vacant=[]
for vertical in range(len(matrix)):
	for horizontal in range(len(matrix[vertical])):
		if matrix[vertical][horizontal]==0: vacant.append((vertical,horizontal))
# print("vacant places: ", len(vacant))



# matrix=numpy.matrix(matrix)
v=0
# tries=0
while v<len(vacant):
	# print(numpy.matrix(matrix))
	# time.sleep(0.2)
	# os.system("cls")
	# print(v)
	a=vacant[v][0]
	b=vacant[v][1]
	for i in range(matrix[a][b],10):
		for j in range(0,9):
			if i==matrix[j][b] or i==matrix[a][j]:
				break
		else:
			if not present_in_grid(b,a,i):
				matrix[a][b]=i
				v+=1
				break
	else:
		matrix[a][b]=0
		v-=1
		# v=abs(v)
	# tries+=1
print(numpy.matrix(matrix))
# print(tries)
# input()
