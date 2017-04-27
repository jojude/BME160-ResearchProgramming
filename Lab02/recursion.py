#
# Jude Joseph
# Mon Apr 10
# 2017
#

"""
	Writting methods recursively 

	fib(n) - uses memorization to remember 
	previous solution to the recursive calls on 
	one side of the tree that way we can reuse them'

	time = number of subproblems * time/subproblems
		 = n * O(1)

"""

memo = {}

def fib(n):
	if n in memo :
		return memo[n]
	if n <= 2:
		return 1
	else:
		f = fib(n-1)+fib(n-2)
		memo[n] = f
		return f

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

def main():
	n = int (input("Enter number :"))
	fac = factorial(5)

	print(fib(n))
	print(fac)

main()