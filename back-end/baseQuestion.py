import json

with open('questions.json') as json_file:
    questions = json.load(json_file)

print(questions)
