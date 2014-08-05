#Problem 12: Highly Divisible Triangle Number
#Kyle Verhoog August 4, 2014

#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 
#1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

import math

#def triangle_num_generator(n):
#	S = 0
#	for i in range(0,n+1):
#		S = S + i
#	return S

def tri_num(n):
	return (n/2.0) * (1 + n)

def num_divisors(n):
	N = 2
	for i in xrange(2,int(math.sqrt(n)) + 1):
		if n%i == 0:
			N = N+2
	return N

i = 1
while True:
	if num_divisors(int(tri_num(i))) > 500:
		print(str(tri_num(i)))
		exit()
	i = i + 1

#Ans: 76576500
