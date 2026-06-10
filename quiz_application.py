questions = {
    "What is the capital of Nepal?": "Kathmandu",
    "What is 5 + 5?": "10",
    "What is the color of the sky?": "Blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        score += 1

print("\nQuiz Completed")
print("Score:", score, "/", len(questions))