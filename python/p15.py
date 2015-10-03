#https://projecteuler.net/problem=15
#Lattice paths
#How many such routes are there through a 20×20 grid?
		
def count_routes(n):
	"""Counts the possible number of routes in a n x n grid"""
	# (  n )
	# (    )  = prod_{i=1}^{n}   (n+i)/i
	# ( 2n ) 
	
	result = 1
	for i in range(1,n+1):
		result *= (n+i)/i
		
	return result
	
	
if __name__ == "__main__":
	n = 20
	result = count_routes(n)
	print(result)   #137846528820