#Problem 10: Summation of Primes
#Kyle Verhoog August 2, 2014

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
def prime(n):
	if n == 1: return False
	elif n == 2: return True
	elif n%2 == 0: return False
	else:
		for i in range(3,int(math.sqrt(n))+1):
			if n%i == 0:
				return False
		return True
n = 0
s = 0
while(n < 2000000):
	if prime(n):
		print(n)
		s = s + n
	n = n + 1
print(s) 
