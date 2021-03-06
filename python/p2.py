#https://projecteuler.net/problem=2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib_naive_recursion(n):
	"""Simple standard naive recursion"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
		
def fib_memoization(n):
	"""Simple standard recursion with memoization"""
	cache = {0:0,1:1}
	def fib_helper(n):
		if n in cache:
			return cache[n]
		cache[n] = fib(n-1) + fib(n-2)
		return cache[n]
	return fib_helper(n)
	
def fib(n):
	"""Helper function which returns the fibonacci number"""
	return fib_memoization(n)

def even_sum(seq):
	"""Returns the sum of the even numbers in the given sequence"""
	return sum(number for number in seq if not number % 2)

def fib_generator(max):
	"""Generator function of the fibonacci numbers smaller than the given max"""
	n = 0
	fib_n = fib(n)
	while fib_n < max:
		yield fib_n
		n += 1
		fib_n = fib(n)

		
def even_fib_generator(max):
    a, b = 2, 8 			 # the first two even fibonacci numbers
    while a < max:
        yield a
        a, b = b, 4 * b + a  # the even fibonacci numbers follow the recurrence relation E(n)=4*E(n-1)+E(n-2)
		
if __name__ == "__main__":
	#result = even_sum(fib_generator(4000000))
	result = sum(even_fib_generator(4000000))
	print(result)
	