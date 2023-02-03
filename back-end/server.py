# Serveur Python
import asyncio
import json

import websockets

with open("questions.json", "r") as file:
    data = json.load(file)
for item in data:
    # print("id:", item["id"])
    # print("question:", item["question"])
    # print("options:", item["options"])
    # print("answer:", item["answer"])
    print(json.dumps(item))


async def handle_message(websocket, path):
    while True:
        message = await websocket.recv()
        if message == 'startGame':
            print('Received message: ', message)
            await websocket.send(json.dumps(item))
        elif message == 'choicePlayer':
            print('Player 1 made a choice: ', message)
        elif message == 'choicePlayer2':
            print('Player 2 made a choice: ', message)
        else:
            print('Invalid message: ', message)


start_server = websockets.serve(handle_message, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
