# Creating sets
tags = {"Python", "ML", "Python", "AI", "ML"}
print(tags)

nums = set([1, 2, 2, 3, 3, 3, 4])
print(nums)

# 0(1) membership test
vocab = set (["hello", "universe", "python"])
print("python" in vocab)
print("java" in vocab)

# set operations
a = {1, 2, 3, 4, 56}
b = {1, 2, 3, 4, 56}

print(a&b)
print(a|b)
print(a-b)