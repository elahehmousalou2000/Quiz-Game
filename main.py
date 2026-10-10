questions = [
    ("What is 2 + 2?", "4"),
    ("Which language are we learning?", "python"),
    ("What keyword creates a function?", "def"),
]

score = 0

for question, answer in questions:
    user_answer = input(question + " ").strip().lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. Answer: {answer}")

print(f"Score: {score}/{len(questions)}")
