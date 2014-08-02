#Problem 2: Even Fibonacci Numbers
#Kyle Verhoog July 30, 2014

#By considering the terms in the sequence whose values do not exceed four million,
#find the sum of the even-valued terms

n_inc = 1
s = 0
n = 1
while (n < 4000000):
	x = n
	n = n + n_inc
	n_inc = x
	if n%2==0 and n < 4000000:
		s = s + n
print(s)
	
		
