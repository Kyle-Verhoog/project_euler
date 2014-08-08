#Problem 16: Power Digit Sum
#Kyle Verhoog August 6, 2014

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

def power_digit_sum(n):
	s = str(n)
	S = 0
	for i in range(0,len(s)):
		S += int(s[i])
	return S

print(power_digit_sum(2**1000))

#Ans: 1366