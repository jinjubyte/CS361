# Author: Brandy Williams
# GitHub username: jinjubyte
# Date: 5/6/2024
# Description: Sprint 1 Main Program Implementation Milestone #1

results = []
selection = []


def intro():
    """Introduction for the main program"""
    print(" _____  __ __  __  ____    _____  __  __ __  _____ ")
    print(" || ||  || ||  ||    //      |    ||  |\ /|  ||    ")
    print(" || ||  || ||  ||   //       |    ||  | | |  ||___ ")
    print(" || ||  ||_||  ||  //        |    ||  || ||  ||    ")
    print(" \__/\  |___|  __  ____      |    ||  || ||  ||___ ")
    print("")

    introduction = ["This program presents a personality quiz ",
                    "involving several multiple choice questions ",
                    "that will determine your personality type.",
                    "",
                    "This quiz will take approximately 5 minutes.",
                    "",
                    "Enter 'Play' to start (This will start the quiz immediately.)",
                    "Enter 'Quit' to exit the program."]

    for line in introduction:
        print(line)


def start_quiz(selection):
    """Main Quiz program with questions and answers"""
    print("Question 1: What is your favorite color?")
    print("Blue")
    print("Red")
    print("Purple")
    print("Yellow")

    selection += input()

    print("Question 2: What is your favorite season?")
    print("Spring")
    print("Summer")
    print("Autumn")
    print("Winter")

    selection += input()

    print("Question 3: What's your favorite vacation location?")
    print("Forest")
    print("Beach")
    print("Urban Cities")
    print("Countryside Villas")

    selection += input()

    print("Thank you for taking the quiz! Here are your results: ")
    print("The Ray of Sunshine")
    print("Your personality type is warm and friendly.")
    print("People naturally gravitate to you and you may find yourself surrounded with many friends.")
    print("")

    repeat_input = input("Try Again? Enter Yes or No")
    if repeat_input.lower() == "yes":
        selection.clear()
        start_quiz(selection)
    elif repeat_input.lower() == "no":
        quit()


# Start program
intro()

while True:
    option = input()
    if option == "Play" or option == 'play':
        start_quiz(selection)
    elif option == "Quit" or option == "quit":
        print("Are you sure you want to exit?")
        response = input("Enter Yes or No")
        if response.lower() == "yes":
            quit()
        elif response.lower() == "no":
            intro()


