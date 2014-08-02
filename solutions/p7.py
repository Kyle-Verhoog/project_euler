#Problem 7: 10001st Prime
#Kyle Verhoog August 1, 2014

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
import math
def prime(n):
	if n == 2: return True
	elif n == 1: return False
	elif n%2 == 0: return False
	else:
		for i in xrange(2,int(math.sqrt(n))+1):
			if n%i == 0:
				return False
		return True
n = 1
i = 1
while True:
	if prime(i):
		if n == 10001:
			break
		n = n + 1
		print(str(i))
	i = i + 2
#Ans: 104743