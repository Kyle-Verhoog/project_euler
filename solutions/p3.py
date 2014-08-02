#Problem 3: Largest Prime Factor
#Kyle Verhoog Aug 1, 2014

#The prime factors of 13195 are 5, 7, 13 and 29
#What is the larget prime factor of the number 600851475143?
import math
n = 600851475143
for i in xrange(int(math.sqrt(n)),2,-1):
	if(n%i == 0): 
		NOT_PRIME = False
		for x in xrange(2,i): 
			if(i%x == 0): 
				NOT_PRIME = True
		if NOT_PRIME == False:
			print(i)
			exit()
