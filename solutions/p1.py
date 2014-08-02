#Problem 1: Multiples of 3 and 5
#Kyle Verhoog July 30, 2014

#If we list all the natural numbers below 10 that are multiples of 3 and 5
#we get 3, 5, 6 and 9. The sum of the multiples is 23. 
#Find the sum of all the multiples of 3 and 5 below 1000. 
s = 0
u = 1000
for i in range(0,u):
	if(i%3 == 0) or (i%5 == 0):
		s = s + i
print(s)
#Ans: 233168