def perfN(n):
	l = []
	for i in range(1, (n/2) + 1):
		if n%i == 0:
			l.append(i)
	
	s = 0
	for i in range(0, len(l)):
		s = s + l[i]
	
	if s == n:
		return True
	else:
		return False


for i in range(2, 100000,2):
	if perfN(i):
		print(i)