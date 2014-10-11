def seqSum(n):

	total = 0
	i = 0;

	while i <= n:
		total += i;
		i += 1;

	return total

def recSum(n):
	if n == 0 : return 0
	else: return n + recSum(n-1)

n = 100

print(seqSum(n))
print(recSum(n))

