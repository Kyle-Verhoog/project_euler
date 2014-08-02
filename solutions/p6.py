#Problem 6: Sum Square Difference
#Kyle Verhoog August 1, 2014

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum(l):
	s = 0
	for i in range(0, len(l)):
		s = s + l[i]
	return s
l1 = []
l2 = []
for i in range(1,100+1):
	l1.append(i)
	l2.append(i**2)
print(sum(l1)**2 - sum(l2))