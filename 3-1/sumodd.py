def sumOdds(n):

	if n == 1: return 1;
	if n == 2: return 1;

	if n % 2 == 0: return sumOdds(n-1);
	else: return n + sumOdds(n-2);

print(sumOdds(39))

