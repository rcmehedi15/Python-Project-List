quiz = {
    "question1": {
        "question": "Which one is the first search engine in internet?",
        "answer": "Archie"
    },
    "question2": {
        "question": "Number of bit used by the IPv6 address?",
        "answer": "128"
    },
    "question3": {
        "question": "Which one is the first web browser invented in 1990?",
        "answer": "Nexus"
    },
    "question4": {
        "question": "First computer virus is known as?",
        "answer": "Creeper Virus"
    },
    "question5": {
        "question": "Firewall in computer is used for?",
        "answer": "Security"
    },
}
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer :')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your Score is: " + str(score))
    else:
        print("Wrong!")
        print("The Answer is : "+value['answer'])
        print("Your Score is : " + str(score))