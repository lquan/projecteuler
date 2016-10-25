#https://projecteuler.net/problem=28
#Number spiral diagonals

def sum_spiral_diagonals(n):
    s = (n-1) // 2
    return (16*s*s*s + 30*s*s + 26*s + 3) // 3
		
		
if __name__ == "__main__":
	n = 1001
	print(sum_spiral_diagonals(n))
	