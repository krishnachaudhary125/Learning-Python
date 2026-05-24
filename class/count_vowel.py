# Count Vowels in Sentence
# Count the total number of vowels (a,e,i,o,u) in a user-entered sentence. Case-insensitive.

sentence = input("Enter sentence: ")
count = 0
vowels = "aeiou"
for char in sentence.lower():
    if char in vowels:
        count += 1
print("Vowels:", count)