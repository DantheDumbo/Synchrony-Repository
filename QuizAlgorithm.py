def hockey_quiz():
    questions = {
        "1. How many players are on the ice for each team in a standard hockey game?": "6",
        "2. What is the name of the area where the goalie stands?": "crease",
        "3. What piece of equipment do players use to hit the puck?": "stick",
        "4. How many periods are there in a regulation hockey game?": "3",
        "5. What is it called when a player scores three goals in one game?": "hat trick",
        "6. What type of shot involves slapping the puck with full force?": "slapshot",
        "7. What is the area between a goalie’s legs called?": "five hole",
        "8. What is the name of the trophy awarded to the NHL champions?": "stanley cup",
        "9. What is it called when the puck crosses two red lines without being touched?": "icing",
        "10. Which position is responsible for blocking shots from entering the net?": "goalie"
    }

    score = 0
    streak = 0
    highest_streak = 0

    for question, correct_answer in questions.items():
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            score += 1
            streak += 1
            print(f"Correct! Your current streak is {streak}.\n")
            if streak > highest_streak:
                highest_streak = streak

        else:
            streak = 0 
            print(f"Wrong! The correct answer was '{correct_answer}'. Your streak has been reset.\n")

    print(f"Game over! You got {score} out of 10 correct.")
    print(f"Your longest streak was {highest_streak} consecutive correct answers.")


hockey_quiz()