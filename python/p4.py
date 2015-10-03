#https://projecteuler.net/problem=4
#Largest palindrome product
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
	"""Checks whether the given input num is a palindrome"""
	x = str(num)
	return x == x[::-1]
	
def largest_palindrome_product(n):
	"""Finds the largest palindrome product of n-digit numbers"""
	result = 0
	a = 10**n - 1 			#n=3 -> 999
	min_num = 10 ** (n -1)  #n=3 -> 100
	while a >= min_num:
		b = 10**n - 1
		while b >= a:
			product = a * b
			if product <= result:
				break
			if is_palindrome(product):
				result = product
			
			b -= 1
		a -= 1
	return result
		
		
if __name__ == "__main__":
	n = 3
	result = largest_palindrome_product(n)
	print(result)
	