from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

print(question_data)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_wrong_answers = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, question_wrong_answers)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")