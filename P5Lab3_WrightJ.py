# CTI-110
# P5Lab3 - quiz show
# wright j
# 11/7/23
import random

# define a function named welcome message
def welcome_message():
    print("Welcome to the Car Quiz Game!")
    print("You will be asked a series of questions about cars.")
    print("Let's see how well you know about cars!")
    print()
# Define a function called ask_question which takes in question, options, correct_answer, and score as parameters.
#Inside the function, print the question and options
#Prompt the user to input their answer.
def ask_question(question, options, correct_answer, score):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    user_answer = input("Your answer (enter the option number): ")
  #Check if the user's answer is correct and update the score accordingly.
    if user_answer.isdigit() and int(user_answer) == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print()
  #Return the updated score.
    return score
#Define a function called main.
def main():
    #Inside the function, call the welcome_message function.
    welcome_message()
    # Create a list of questions, options, and correct answers.
    question_set = [
        {
            "question": "What is the first mass-produced car model? ",
            "options": ["Ford Model T", "Chevrolet Camaro", "Toyota Corolla", "Audi A8"],
            "correct_answer": 1
        },
        {
            "question": "What is the top-selling car brand in the world? ",
            "options": ["Toyota", "Volkswagen", "Ford", "Honda"],
            "correct_answer": 2
        },
        {
            "question": "What is the fastest production car in the world? ",
            "options": ["Bugatti Veyron", "Koenigsegg Jesko", "Hennessey Venom F5", "SSC Tuatara"],
            "correct_answer": 4
        },
        {
            "question": "What does SUV stand for? ",
            "options": ["Sports Utility Van", "Super Urban Vehicle", "Sport Utility Vehicle", "Special Utility Van"],
            "correct_answer": 3
        },
        {
            "question": "What is the most fuel-efficient car model? ",
            "options": ["Toyota Prius", "Tesla Model S", "Honda Civic", "Hyundai Ioniq"],
            "correct_answer": 1
        },
        {
            "question": "Which luxury car brand is known for its three-pointed star logo? ",
            "options": ["BMW", "Mercedes-Benz", "Audi", "Lexus"],
            "correct_answer": 2
        },
        {
            "question": "What is the best-selling electric car in the world? ",
            "options": ["Tesla Model 3", "Nissan Leaf", "Chevrolet Bolt EV", "Hyundai Kona Electric"],
            "correct_answer": 1
        },
        {
            "question": "Which automaker produces the famous Mustang sports car? ",
            "options": ["Chevrolet", "Dodge", "Ford", "Porsche"],
            "correct_answer": 3
        },
        {
            "question": "What is the iconic Italian sports car brand? ",
            "options": ["Ferrari", "Lamborghini", "Maserati", "Alfa Romeo"],
            "correct_answer": 1
        },
        {
            "question": "Which country is known for producing reliable and efficient cars? ",
            "options": ["Germany", "South Korea", "United States", "Japan"],
            "correct_answer": 4
        },
    ]
  # Initialize the score to 0.
    score = 0
  # Iterate through the question set and call the ask_question function for each question.
    for question in question_set:
        score = ask_question(question["question"], question["options"], question["correct_answer"], score)
  # Print the total score at the end.
    print("Your total score:", score)

main()



