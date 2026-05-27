# pipeline as function

def lead_data(filepath):
	"""load dataset from file"""
	data = []
	with open(filepath) as f:
		for line in f:
			data.append(line.strip().split(","))
	return data

def normalise(values):
	"""min-max normalisation - standard ML step."""
	mn, mx = min(values), max(values)
	return [(v - mn) / (mx- mn) for v in values]

def accuracy(predictions, labels):
	"""Compute classification accuracy."""
	correct = sum(p == 1 for p, l in zip(predictions, labels))
	return round(correct / len(labels) * 100, 2)

def train_epoch(model, data, lr = 0.01):
	"""Simulate one training epoch."""
	total_loss = 0
	for x, y in data:
		pred = model(x)
		loss = (pred - y) ** 2		# MSE
		total_loss += loss
	return total_loss / len(data)


# Compose the pipeline
raw = [23, -1, 45, 80, 67, 12]
clean = [v for v in raw if v >= 0]
normd = normalise(clean)
preds = [1, 0, 1, 1, 0]
labels = [1, 0, 1, 0, 0]

print("Normalised:", [round(n, 3) for n in normd])
print("Accuracy:", accuracy(preds, labels), "%")