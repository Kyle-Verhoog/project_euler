#Problem 18: Maximum Path Sum I
#Kyle Verhoog August 6, 2014

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
#                    75                                                         0        +1,+2
#                   95 64                                                     01 02      +2,+3
#                 17 47 82                                                   03 04 05    +3,+4
#                18 35 87 10                                               06 07 08 09   +4,+5
#               20 04 82 47 65                                            10 11 12 13 14
#              19 01 23 75 03 34
#            88 02 77 73 07 63 67
#           99 65 04 28 06 16 70 92
#          41 41 26 56 83 40 80 70 33
#        41 48 72 33 47 32 37 16 94 29
#       53 71 44 65 25 43 91 52 97 51 14
#      70 11 33 28 77 73 17 78 39 68 17 57
#     91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
#  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# Find the maximum total from top to bottom of the triangle below:

s="                75\
                  95 64\
                17 47 82\
               18 35 87 10\
              20 04 82 47 65\
             19 01 23 75 03 34\
           88 02 77 73 07 63 67\
          99 65 04 28 06 16 70 92\
         41 41 26 56 83 40 80 70 33\
       41 48 72 33 47 32 37 16 94 29\
      53 71 44 65 25 43 91 52 97 51 14\
     70 11 33 28 77 73 17 78 39 68 17 57\
    91 71 52 38 17 14 91 43 58 50 27 29 48\
  63 66 04 68 89 53 67 30 73 16 69 87 40 31\
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"


def max_sum(t):
	t = t.replace(" ", "")
	p = []
	for i in range(0,len(t),2): #put the data into a list representing the positions
		p.append(int(str(t[i]) + str(t[i+1])))
	print(tastypath(p))
	print(sum(tastypath(p)))
	
def sum(l):
	S = 0
	for i in range(0, len(l)):
		S += l[i]
	return S

def tastypath(p):
	inc = 1
	l = []
	l.append(p[0]) #put the first position into the path list
	cur_index = 0
	while cur_index+inc+1 < len(p):
		if p[cur_index+inc] > p[cur_index+inc+1]:
			l.append(p[cur_index+inc])
			cur_index = cur_index+inc
		else:
			l.append(p[cur_index+inc+1])
			cur_index = cur_index+inc+1
		inc += 1
	return l









print(max_sum(s))

input()






