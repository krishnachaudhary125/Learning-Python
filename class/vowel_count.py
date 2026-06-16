text = "Hello World!!"

vo = 0
consonants = 0
vowel = ["a", "e", "i", "o", "u"]

for char in text:
	if char in vowel:
		vo += 1
	else:
		consonants += 1

print("Vowel =",vo,"\nConsonants =",consonants)