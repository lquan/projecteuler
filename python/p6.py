#https://projecteuler.net/problem=6
#Sum square difference
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_arithmetic(n):
	"""Returns the arithmetic sum of the natural numbers <= n"""
	#return sum(i for i in range(n+1))
	return n*(1+n)/2

def sum_of_squares(n):
	"""Returns the sum of squares of the natural numbers <= n"""
	#return sum(i**2 for i in range(n+1))
	return n/6*(2*n+1)*(n+1)
	
def sum_square_difference(n):
	"""Finds the sum square difference of the natural numbers <= n"""
	sum_squares = sum_of_squares(n)
	sum_squared = sum_arithmetic(n) ** 2
	return sum_squared - sum_squares
		
		
if __name__ == "__main__":
	n = 100
	result = sum_square_difference(n)
	print(result)
	