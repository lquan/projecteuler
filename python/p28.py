#https://projecteuler.net/problem=28
#Number spiral diagonals

def spiral_diagonals(n):
	i = 1
	yield i
	
	level = 1;
	while level < n - 2:
		yield i + 2 * level
		yield i + 4 * level
		yield i + 6 * level
		yield i + 8 * level
		
		i = i + 8 * level
		level += 1
		
		
def sum_spiral_diagonals(n):
	return sum(spiral_diagonals(n))
		
if __name__ == "__main__":
	n = 1001
	#print([x for x in spiral_diagonals(n)])
	print(sum_spiral_diagonals(n))
	