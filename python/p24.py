#https://projecteuler.net/problem=24
#Lexicographic permutations
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations, islice

def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(islice(iterable, n - 1, None), default)
	
def find_nth_permutation(n, list):
	"""Returns the n-th lexicographic permutation of the items in the list"""
	return nth(permutations(list), n)
	  
if __name__ == "__main__":
	n = 1000000
	numbers = range(0,10)
	result = find_nth_permutation(n, numbers)
	print(result)  #2783915460
