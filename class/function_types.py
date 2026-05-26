# Positional
def add(a, b):
	return a + b
print(add(3, 5))


# Default
def greet(name, msg="Hi!"):
	print(msg, name)
greet("Krishna")
greet("Sumit")
greet("Subodh")


# keyword
def info(name, age, city):
	print(name, age, city)
info(age=21, city="Lalitpur", name="Krishna")


# args / **kwargs
def total(*nums):
	return sum(nums)
def show(**info):
	for k, v in info.items():
		print(k, v)