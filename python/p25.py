#https://projecteuler.net/problem=25
#What is the first term in the Fibonacci sequence to contain 1000 digits?
from math import log10, sqrt, ceil

def fibonacci_digits(n):
	"""Returns the first Fibonacci number with n digits"""
	phi = (1+sqrt(5))/2
	return int(ceil((n-1 + log10(5)/2) /log10(phi))) #using Binet and https://en.wikipedia.org/wiki/Logarithm#Particular_bases
		
if __name__ == "__main__":
	n = 1000
	print(fibonacci_digits(n))
	