import json

with open("questions.json", "r") as file:
    data = json.load(file)

for item in data:
    print("Question: ", item["question"])
    print("Correct answer: ", item["correct_answer"])
    print("Incorrect answers: ", item["incorrect_answers"])
    print("---")
