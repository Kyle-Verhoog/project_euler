#Problem 15: Lattice Paths
#Kyle Verhoog August 5, 2014


#function works for first couple lattice structures, breaks down after that :(
# def lattice(g):
# 	n = 1
# 	for i in range(1,g):
# 		n += g*i
# 	n *= 2
# 	print(n) 


#Using Every other row of Pascal's Triangle yields the nth number of paths

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)
def paths(g):
	return (fact(2*g)) / (fact(g)**2)

print(paths(20))
#Ans: 137846528820 
