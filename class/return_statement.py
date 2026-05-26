# Return a single value
def square(n):
	return n ** 2

# Return multiple values (tuple unpacking)
def min_max(nums):
	return min(nums), max(nums)

# Return ends the function immediately
def check_age(age):
	if age < 0:
		return "Invalid" # exits here
	if age < 18:
		return "Minor"
	return "Adult" # Only if above two skipped

# Using the returns
print(square(7))
lo, hi = min_max([4, 1, 9, 2, 7])
print(f"Min = {lo}, Max = {hi}")
print(check_age(21))