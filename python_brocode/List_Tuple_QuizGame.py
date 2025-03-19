# Quiz Game:

questions = (
    "What is the capital of France?",
    "Who wrote 'Hamlet'?",
    "What is the largest planet in our solar system?",
    "How many continents are there on Earth?",
    "What is the chemical symbol for gold?",
    "Who was the first person to walk on the moon?",
    "Which is the longest river in the world?",
    "What is the national currency of Japan?",
    "Who discovered gravity?",
    "What is the boiling point of water in Celsius?"
)

options = (
    ("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"),
    ("A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"),
    ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"),
    ("A) Five", "B) Six", "C) Seven", "D) Eight"),
    ("A) Ag", "B) Au", "C) Pb", "D) Fe"),
    ("A) Buzz Aldrin", "B) Yuri Gagarin", "C) Neil Armstrong", "D) Michael Collins"),
    ("A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"),
    ("A) Yen", "B) Won", "C) Rupee", "D) Peso"),
    ("A) Albert Einstein", "B) Isaac Newton", "C) Galileo Galilei", "D) Nikola Tesla"),
    ("A) 90°C", "B) 100°C", "C) 120°C", "D) 80°C")
)
answers = ("C", "B","C","C","B","C","B","A","B","B")

guesses = []
score = 0
question_num =0

for question in questions:
    print("=======================================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer:")
    guesses.append(guess)
    if guess.lower() == answers[question_num].lower():
        print("correct!")
        score +=1
    else:
        print("incorrect!")
    question_num += 1
print(f"Total Score:{score} out of {len(questions)}")