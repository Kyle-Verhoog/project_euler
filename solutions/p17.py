#Problem 17: Number Letter Counts
#Kyle Verhoog August 6, 2014

#If the number 1 to 5 are written out in words: 
#one, two, three, four, five, then there are 3+3+5+4+4=19 letters used in total

#If all the number from 1 to 1000 inclusive were written out in words, how many letters would be used

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
#115 (one hundred and fifteen) contains 20 letters. 
#The use of "and" when writing out numbers is in compliance with British usage. 

str_stupid_english = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
str_naming = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
str_higher = ["one", "hundred","thousand","million","billion"]
str_and = "and"

def sum():
	S = 0
	for i in range(1,100):
		if i < 20 and i != 10:
			S += len(str_stupid_english[i])
		if i > 20 and i < 100:
			S += len(str_stupid_english[int(str(i)[1])]) + len(str_naming[int(str(i)[0])])
	S *= 10

	for x in range(1,10):
		S += len(str_stupid_english[x]) * 100 

	S += len(str_and) * (900-9)
	S += len(str_higher[1]) * 900
	S += len(str_stupid_english[1]) + len(str_higher[2])
	return S

print(sum())



	# if i > 100:
	# 	S += len(str_higher[int(len(str(i)) -1)])
	# 	S += len()






	# if i < 1000 and str(i).endswith("00"):
	# 	S += len(str_higher[0]) + len(str_stupid_english[int(str(i)[0])])
	# 	print(str_stupid_english[int(str(i)[0])] + str_higher[0])
	# elif i > 100 and i < 1000:
	# 	if str(i)[1] == 1:
	# 		S += len(str_higher[0]) + len(str_stupid_english[int(str(i)[0])+10]) + len(str_stupid_english[int(str(i)[2])]) + len(str_naming[int(str(i)[1])]) + len(str_and)
	# 		print("fdSFDASFDAS")
	# 	else:
	# 		S += len(str_higher[0]) + len(str_stupid_english[int(str(i)[0])]) + len(str_stupid_english[int(str(i)[2])]) + len(str_naming[int(str(i)[1])]) + len(str_and)
	# 		print(str_stupid_english[int(str(i)[0])] + str_higher[0] + str_and + str_naming[int(str(i)[1])] + str_stupid_english[int(str(i)[2])])

	
	# if i == 1000:
	# 	S += len(str_higher[1]) + len(str_stupid_english[int(str(i)[0])])
	# 	print(str_stupid_english[int(str(i)[0])] + str_higher[1])









