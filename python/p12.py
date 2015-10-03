#https://projecteuler.net/problem=12
#Highly divisible triangular number
#What is the value of the first triangle number to have over five hundred divisors?

def triangle_number(n):
	return n * ( n + 1) // 2
			
def triangle_number_generator():
	n = 1
	while True:
		yield triangle_number(n)
		n += 1
	
if __name__ == "__main__":
	n = 500
	#result = sum(sieve_eratosthenes(n))
	#print(result)
	