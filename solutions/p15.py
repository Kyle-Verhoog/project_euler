#Problem 15: Lattice Paths
#Kyle Verhoog August 5, 2014


#function works for first couple lattice structures, breaks down after that :(
def lattice(g):
	n = 1
	for i in range(1,g):
		n += g*i
	n *= 2
	print(n) 

