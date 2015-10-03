#https://projecteuler.net/problem=20
#Factorial digit sum
#Find the sum of the digits in the number 100!
import math

def factorial(n):
	"""Returns n!, the factorial of n"""
	return math.factorial(n)
	
	
if __name__ == "__main__":
	n = 100
	num = factorial(n)
	result = sum(int(i) for i in str(num))
	print(result)