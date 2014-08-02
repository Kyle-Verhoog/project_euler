#Problem 4: Largest Palindrome Product
#Kyle Verhoog August 1, 2014

#A palindrome number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers

def reverse(s):
	r = ""
	for i in range(len(s)-1,-1,-1):
		r = r + s[i]
	return r

digits = 3
l = []
for i in range(10**(digits-1),10**digits):
	for x in range(10**(digits-1),10**digits):
		s = str(i*x)
		if s == reverse(s):
			l.append(i*x)

k = 0
for i in range(0,len(l)-1):
	if l[i] > k:
		k = l[i]
print(k)

#Ans: 906609