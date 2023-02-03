import asyncio
import json
import websockets

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_wrong_answers = question["incorrect_answers"]
    new_question = Question(
        question_text, question_answer, question_wrong_answers)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

clients = set()


async def handle_connection(websocket, path):
    clients.add(websocket)
    while True:
        message = await websocket.recv()
        message = json.loads(message)
        if message["type"] == "answer":
            is_correct = quiz.check_answer(message["answer"])
            response = {"type": "answer_result", "is_correct": is_correct}
            response_json = json.dumps(response)
            await websocket.send(response_json)
        if message["type"] == "request_question":
            question, answers = quiz.next_question()
            response = {"type": "question",
                        "question": question, "answers": answers}
            response_json = json.dumps(response)
            await websocket.send(response_json)
    clients.remove(websocket)

start_server = websockets.serve(handle_connection, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
