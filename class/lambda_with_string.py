# Lambda for string transformations
upper = lambda s: s.upper()
print(upper("Hello"))

# Sorting strings by length
words = ["banana", "apple", "mango", "grape", "cherry"]
words.sort(key = lambda w: len(w))
print(words)

# Using map() with lambda
names = ["Krishna", "Sumit", "Subodh"]
titled = list(map(lambda n: n.title(), names))
print(titled)

# filter: words longer than a chars
long_w = list(filter(lambda w: len(w)>4, words))
print(long_w)