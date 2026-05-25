# ML Accuracy Tracker
# Simulate training: each epoch, accuracy increases by a random delta. Stop when accuracy ≥ 95% or epoch > 50. Print epoch summary.

import random

random.seed(42)

accuracy = 60.0
epoch = 0

while accuracy < 95 and epoch <= 50:
    epoch += 1
    accuracy += random.uniform(0.5, 3.0)

    status = "✔" if accuracy >= 95 else " "

    print(f"Epoch {epoch:>2}: {accuracy:>5.1f}% {status}")

print(f"\nDone in {epoch} epochs")