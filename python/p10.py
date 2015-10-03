#https://projecteuler.net/problem=10
#Summation of primes
#Find the sum of all the primes below two million.

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
			
	
if __name__ == "__main__":
	n = 2000000
	result = sum(sieve_eratosthenes(n))
	print(result)
	