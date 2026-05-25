# Guess the Secret Number
# Secret number is 42. User keeps guessing. Give Too High / Too Low hints. Count attempts.

secret = 42
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess > secret:
        print("Too High!")
    else:
        print("Too Low!")