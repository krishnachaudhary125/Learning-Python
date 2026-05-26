# Function that processes a list
def find_evens(numbers):
	evens = []
	for n in numbers:
		if n % 2 == 0:
			evens.append(n)
	return evens


# Functions that builds a multiplication table
def time_table(n, limit = 10):
	result = []
	for i in range(1, limit +1):
		result.append(f"{n} x {i} = {n*i}")
	return result


# Function to flatten nested list (AI data use)
def flatten(nested):
	flat = []
	for sublist in nested:
		for item in sublist:
			flat.append(item)
	return flat

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(find_evens(data))
print(time_table(3, 5))
print(flatten(matrix))