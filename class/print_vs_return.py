# Using print() - Broken
def add(a, b):
	print(a + b) # Just shows on screen

result = add(3, 4)
print(result) # What prints?
final = result + 10 # CRASH!
print(final)


# Using return - Correction
def add(a, b):
	return a + b # hands back value

result = add(3, 4)
print(result) # shows 7
final = result + 10 # works!
print(final)