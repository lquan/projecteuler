#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def naive(n):
	return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


def sum_divisible_by(k, n):
	"""calculate the sum of the numbers less than n that are divisible by k"""
	p = n // k
	return k * (p * (p+1)) // 2
	
def better(n):
	"""calculate the sum of the numbers less than n that are divisible by 3,
	plus the sum of the numbers less than n that are divisible by 5
	minus the sum of the numbers less than n divisible by both (15)
	"""
	return sum_divisible_by(3, n) + sum_divisible_by(5, n) -  sum_divisible_by(15, n) # by inclusion-exclusion principle
	
	
if __name__ == "__main__":
	n = 10000
	print(naive(n))
	print(better(n))

	