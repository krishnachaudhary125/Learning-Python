txt = "	Hello, World!!	"

clean = txt.strip().lower()
print(clean)

words = clean.replace(",", "").split()
print(words)

reverse = clean[::-1]
print(reverse)

sentence = "subodh is dragon"
word_freq = {o: sentence.split().count(o) for o in sentence.split()}
print(word_freq)