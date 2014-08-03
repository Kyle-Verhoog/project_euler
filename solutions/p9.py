#Problem 9: Special Pythagorean Triplet
#Kyle Verhoog August 2, 2014

#A Pythagorean Triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.

#Find the product abc. 
u = 1000
for a in range(100,u):
	for b in range(a+1,u):
		for c in range(b+1,u):
			if (a**2 + b**2) == (c**2) and (a+b+c) == 1000:
				print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
				print(a*b*c)
				exit()

#Ans: 200^2 + 375^2 = 425^2
#Ans: abc = 31875000