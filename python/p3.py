#https://projecteuler.net/problem=3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(n):
	"""Finds the largest prime factor of the given number n"""
	k = 2
	while k * k <= n: # every number n can at most have one prime factor greater than sqrt(n)
		#For each k, if it is a factor of n then we divide n by k and completely divide out each k before moving to the next k
		if n % k == 0:
			n //= k
		else:
			k += 1
	return n
		
if __name__ == "__main__":
	n = 600851475143
	result = largest_prime_factor(n)
	print(result)
	