catalog = {"apple":1.5, "mango":2.0, "banana":0.8}

# Dictionary comprehension (Pythonic)
expensive = {k:v for k,v in catalog.items() if v>1.0}
print(expensive)

# Merge two dicts (Python 3.9+)
extras = {"grape":3.0, "lime":1.2}
catalog.update(extras)

# Count word frequency (classic NLP)
text = "the cat sat on the mat the cat"
freq = {}
for word in text.split():
	freq[word] = freq.get(word, 0) + 1
print(freq)