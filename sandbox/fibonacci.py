# Author: Joshua
#
# Notes: Print out the nth fibonacci number

def fib(n):
	if n <= 0:
		return 1
	return fib(n-1) + fib(n-2)
var = input("Print the Nth fibonacci number! N = ? -> ")
print(fib(var))
