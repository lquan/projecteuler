#https://projecteuler.net/problem=23
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from itertools import product
from collections import Counter
from operator import mul
from functools import reduce

def gen_primes():
    """ Generate an infinite sequence of prime numbers."""
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1
			
def prime_factors(num):
   """Get prime divisors with multiplicity"""

   pf = Counter()
   primes = gen_primes()
   while num > 1:
      p = next(primes)
      m = 0
      while m == 0:
         d,m = divmod(num,p)
         if m == 0:
            pf[p] += 1
            num = d
   return pf

def prod(l):
   return reduce(mul, l, 1)

def powered(factors, powers):
   return prod(f**p for (f,p) in zip(factors, powers))


def divisors(num):
   pf = prime_factors(num)
   primes = pf.keys()
   #For each prime, possible exponents
   exponents = [range(i+1) for i in pf.values()]
   return sorted([powered(primes,es) for es in product(*exponents)])
   
def proper_divisors(num):
	return divisors(num)[:-1]

def is_abundant(num):
	return False
   
if __name__ == "__main__":
	#TODO
	n = 28
	print(divisors(n))
	