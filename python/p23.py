#https://projecteuler.net/problem=23
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from bisect import bisect
from itertools import islice
def all_sum_divisors(n):
    """Return a list of the sums of divisors for the numbers below n.

    >>> all_sum_divisors(10) # https://oeis.org/A000203
    [1, 1, 3, 4, 7, 6, 12, 8, 15, 13]

    """
    result = [1] * n
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m
                    result[i] *= m
                last_m = m
                p_power *= p
    return result
	
def solve_euler23(n=28124):
    """Return the sum of all positive integers below n which cannot be
    written as the sum of two abundant numbers.
    """
    sum_divisors = all_sum_divisors(n)
    abundant = [i for i in range(1, n) if sum_divisors[i] > 2 * i]
    abundant_set = set(abundant)
    def unsums():
        for i in range(1, n):
            for j in islice(abundant, bisect(abundant, i // 2)):
                if i - j in abundant_set:
                    break
            else:
                yield i
    return sum(unsums())
   
if __name__ == "__main__":
	print(solve_euler23())
	