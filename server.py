# Serveur Python
import asyncio
import websockets


testMsg = {"Message" : "test", "question" : "1"}
async def handle_message(websocket, path):
    while True:
        message = await websocket.recv()
        if message == 'startGame':
            print('Received message: ', message)
            await websocket.send(str(testMsg))
        elif message == 'choicePlayer':
            print('Player 1 made a choice: ', message)
        elif message == 'choicePlayer2':
            print('Player 2 made a choice: ', message)
        else:
            print('Invalid message: ', message)

start_server = websockets.serve(handle_message, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
