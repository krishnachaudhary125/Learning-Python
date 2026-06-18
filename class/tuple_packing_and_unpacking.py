# Packing (implicit)
student = "Krishna", 21, 92.5		# Creation tuple

# Unpacking
name, age, score = student
print(name, age, score)

# Extended unpacking (*)
first, *rest = [10, 20, 30, 40, 50]
print(first, rest)

# Swap variables (Pythonic!)
a, b = 5, 10
a, b = b, a
print(a, b)

# Function returning multiple values
def min_max(lst):
	return min(lst), max(lst)

lo, hi = min_max([3, 1, 9, 5])
print(lo, hi)