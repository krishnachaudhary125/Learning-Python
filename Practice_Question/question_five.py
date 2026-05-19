# Dataset Normalizer
# Given a list of scores [45,78,92,23,67], normalize to 0–1 using min-max scaling with loops.

scores = [45, 78, 92, 23, 67]

min_val = min(scores)
max_val = max(scores)

normalize = []

for i in scores:
    norm = (i - min_val)/(max_val - min_val)

    normalize.append(norm)

print("Original score :",scores)
print("Normalized score :",normalize)