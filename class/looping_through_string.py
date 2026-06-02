text = "HELLO"

for ch in text:
	print(ch, end=" ")

for i, ch in enumerate(text):
	print(f"{i}:{ch}", end=" ")

vowels = [c for c in text if c in "AEIOU"]
print(vowels)