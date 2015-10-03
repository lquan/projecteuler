#https://projecteuler.net/problem=9
#Special Pythagorean triplet
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc
from numpy import mat, array


def gen_pythagorean_triples(max):
    """generate all primative triples such that
    the hypotenuse is less than or equal to max"""
    u = mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = mat(' 1  2  2;  2  1  2; 2 2 3')
    d = mat('-1 -2 -2;  2  1  2; 2 2 3')
    m = [array([3, 4, 5])]
    while m:
        yield from m
        g = ((i*j).getA1() for i in m for j in (u, a, d))
        m = [i for i in g if i[2] <= max]
			
def gen_all_pythagorean_triples(max):
    """generate all triples such that
    the hypotenuse is less than or equal to max"""
    for primitive in gen_pythagorean_triples(max):
        i = primitive[:]
        while i[2] <= max:
            yield i
            i += primitive			

def find_pythagorean_triple_sum(max, n):
	"""finds the triples x,y,z which satisfy x+y+z == n and z <= max"""
	for x,y,z in gen_all_pythagorean_triples(max):
		if x + y + z == n:
			yield x, y, z
			
if __name__ == "__main__":
	max = 10000
	n = 1000
	
	for x, y, z in find_pythagorean_triple_sum(max, n):
		print(x, y, z)
	