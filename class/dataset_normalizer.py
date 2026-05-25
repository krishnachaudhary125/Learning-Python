# Dataset Normaliser (Min-Max)
# Normalise a list of scores to [0.0–1.0] using Min-Max scaling formula: (x–min)/(max–min).

data = [20, 60, 80, 40, 100, 10, 55]

min_val = data[0]
max_val = data[0]

for x in data:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

normalised = []

for x in data:
    n = (x - min_val) / (max_val - min_val)
    normalised.append(round(n, 3))

print(normalised)