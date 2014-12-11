def sumCubes(n):
	if n == 1: return 1;
	return n**3 + sumCubes(n-1)

print(sumCubes(13))
