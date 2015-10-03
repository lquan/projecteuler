#https://projecteuler.net/problem=14
#Longest Collatz sequence
#Which starting number, under one million, produces the longest chain?
import operator

def collatz(n):
	yield n
	while n > 1:
		a, b = divmod(n,2)
		if b == 0:
			n = a
			if a == 1:
				break
		else:
			n = 3 * n + 1
		yield n
		
	yield n
	
def collatz_generator(n):
	"""Generates a sequence of starting numbers and their corresponding collatz chain"""
	return ((i, collatz(i)) for i in range(1,n))
		
def max_collatz_generator(n):
	"""Returns the starting number < n which produces the largest collatz chain 
	and the length of the chain itself
	
	this is a very naive approach as caching the items in the chain will significantly reduce the runtime of the algorithm
	"""
	max_len = 0
	max_num = 0
	for i, collatz in collatz_generator(n):
		chain = list(collatz)
		#print(chain)
		chain_length = len(chain)
		if chain_length > max_len:
			max_len = chain_length
			max_num = i
		
	return max_num, max_len
		
	
if __name__ == "__main__":
	#print(list(collatz(13)))
	max = 1000000
	print(max_collatz_generator(max))