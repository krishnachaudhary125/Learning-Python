import re

# NLP preprocessing Pipeline
text = "Hello! I am Krishna Chaudhary"

# Step 1: Normalize
text = text.lower().strip()

# Step 2: Remove punctuation
text = re.sub(r'[^\w\s]', ' ', text)

# Step 3: Tokenize
tokens = text.split()

# Step 4: Remove stopwords
stops = ('i', 'the', 'a', 'is')
tokens = [t for t in tokens if t not in stops]

print(tokens)