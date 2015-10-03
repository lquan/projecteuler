#https://projecteuler.net/problem=34
#Digit factorials
#Find the sum of all numbers which are equal to the sum of the factorial of their digits (the curious numbers).

def find_curious_numbers(n):
	"""Generates the numbers <= n which are equal to the sum of the factorial of their digits"""
	fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] #precomputed factorials
	for k in range(3, n+1):  #0,1,2 are excluded
		if k == sum(fac[int(i)] for i in str(k)):
			yield k
	  
if __name__ == "__main__":
	n = 9999999 # easy upper limit 7 * 9! <= n
	result = sum(find_curious_numbers(n))
	print(result)