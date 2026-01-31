import random

question_bank = {
    "Python dictionary key must be?": "unique",
    "Which method returns keys?": "keys",
    "Which method returns key-value pairs?": "items",
    "How to safely get missing key?": "get"
}

def play():
    score = 0
    questions = list(question_bank.items())
    random.shuffle(questions)

    for q, ans in questions:
        user = input(q + " ").strip().lower()
        if user == ans:
            score += 1
            print("Correct!")
        else:
            print("Wrong! Answer:", ans)
    print("Score:", score, "/", len(question_bank))

while True:
    play()
    if input("Play again? (y/n): ").lower() != "y":
        break
