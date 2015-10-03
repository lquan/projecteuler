#https://projecteuler.net/problem=7
#10001st prime
#What is the 10 001st prime number?

def sieve_eratosthenes(n):
    """Return all primes <= n"""
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
		

def find_nth_prime(n):
	"""Finds the nth prime number using repeated bounds on the sieve of eratosthenes"""
	limit = 1000
	primes = [1]
	while n - 1 > len(primes):
		primes = list(sieve_eratosthenes(limit))
		limit *= 2 
		
	return primes[n-1]
		
	
if __name__ == "__main__":
	print(list(sieve_eratosthenes(100000)))
	n = 10001
	result = find_nth_prime(n)
	print(result)
	