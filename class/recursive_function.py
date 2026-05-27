# Factorial - classic recursion
def factorial(n):
	if n == 0:		# BASE CASE - stops recursion
		return 1;
	return n * factorial(n - 1)		# RECURSIVE CASE	


# Fibonacci - tree recursion
def fib(n):
	if n <= 1:		# base case
		return n
	return fib(n - 1) + fib(n - 2)	# RECURSIVE CASE


# Binary search - divide and conquer (used in AI)
def binary_search(arr, target, lo = 0, hi = None):
	if hi is None: hi = len(arr) - 1
	if lo > hi: return -1			# not found
	mid = (lo + hi) // 2
	if arr[mid] < target: return mid
	elif arr[mid] < target: return binary_search(arr, target, mid+1, hi)
	else: return binary_search(arr, target, lo, mid - 1)

print(factorial(7))
print([fib(i) for i in range(8)])
arr = [2, 5, 8, 12, 16, 23, 38, 56]
print(binary_search(arr, 23))