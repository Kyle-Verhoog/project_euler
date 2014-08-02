#Problem 5: Smallest Multiple
#Kyle Verhoog August 1, 2014

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder

#What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
x=20
while True:
	smallest_multiple = True
	for i in range(1,21):
		if x%i != 0:
			smallest_multiple = False
	if smallest_multiple == True:
		print x
		exit()
	x = x+2
#Ans: 232792560