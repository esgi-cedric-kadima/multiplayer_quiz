# Serveur Python
import asyncio
import json

import websockets

with open('questions.json') as json_file:
    questions = json.load(json_file)

print(questions)


async def handle_message(websocket, path):
    while True:
        message = await websocket.recv()
        if message == 'startGame':
            print('Received message: ', message)
            await websocket.send(str(questions))
        elif message == 'choicePlayer':
            print('Player 1 made a choice: ', message)
        elif message == 'choicePlayer2':
            print('Player 2 made a choice: ', message)
        else:
            print('Invalid message: ', message)


start_server = websockets.serve(handle_message, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
