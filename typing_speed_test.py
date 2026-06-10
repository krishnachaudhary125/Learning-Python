import time

sentence = "Python is a powerful programming language."

print(sentence)

start = time.time()

user_input = input("\nType the sentence above:\n")

end = time.time()

seconds = end - start

words = len(sentence.split())

wpm = (words / seconds) * 60

print(f"Typing Speed: {wpm:.2f} WPM")