import random

# Quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Which country won the FIFA World Cup in 2018?": "France",
    "Who is the current President of the United States?": "Joe Biden",
    "Which country recently launched a mission to Mars called Perseverance?": "United States",
    "What is the largest ocean on Earth?": "Pacific Ocean"
}

# Function to run the quiz
def run_quiz():
    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)
    
    for question in question_list:
        print(question)
        answer = input("Your answer: ")
        if answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {questions[question]}")
            
        print()
    
    print(f"Quiz completed! You scored {score}/{len(questions)}.")

# Run the quiz
run_quiz()
