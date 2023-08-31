
import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:4453') as websocket:
        message = input("What's your message? ")

        await websocket.send(message)
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received message: {response}")

asyncio.get_event_loop().run_until_complete(hello())
