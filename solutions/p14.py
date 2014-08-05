#Problem 14: Longest Collatz Sequence
#Kyle Verhoog August 4, 2014

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def Collatz(n):
	if n == 1:
		return 1
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

def rCollatz(n):
	if n == 1:
		return 1
	if rCollatz.s == "":
		rCollatz.s = str(n)
	if n%2 == 0:
		rCollatz.s += " -> " + str(n/2)
		return rCollatz(n/2)
	else:
		rCollatz.s += " -> " + str(3*n + 1)
		return rCollatz(3*n+1)

def longest_collatz():
	L = 0
	l = 0
	for i in xrange(999999,1,-2):
		rCollatz.s = ""
		rCollatz(i)
		print(rCollatz.s)
		if len(rCollatz.s) > l:
			L = i
			l = len(rCollatz.s)
	print(L)

longest_collatz()
#Ans: 837799