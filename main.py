questions = ["What is 2 + 2? \n\n A. 4 \n B. 5 \n C.6",
             "What is 2 + 3? \n\n A. 6 \n B. 8 \n C. 5",
             "What is 2 + 1? \n\n A. 4 \n B. 3 \n C. 7"]
answers = ["A", "C", "B"]
cut_off_mark = 50
score = 0

def initiate_cert():
    return "Congratulations! You've earned a certificate."

print("----Welcome to the Quiz App!----")
user_input = input("Enter 'p' to proceed: ")
if user_input.lower() == "p":
    print("--Game Instruction--")
    print("-Instruction 1: Use the designated key (e.g., A, B, C) to choose your answer.")
    print("-Instruction 2: Type the letter and press ENTER to submit your answer.")
    print(" ")

    for i in range(len(questions)):
        print(" ")
        user_answer = input(f"{questions[i]}\n Enter answer: ")
        if user_answer.upper() == answers[i]:
            score += 1

    print(" ")
    result = f"You scored {score} out of {len(questions)}."
    score_per = 100 * (score / len(questions))

    print(result)
    if score_per > cut_off_mark:
        print(initiate_cert())

    print("End of Game")
else:
    print("Goodbye game ended!")
