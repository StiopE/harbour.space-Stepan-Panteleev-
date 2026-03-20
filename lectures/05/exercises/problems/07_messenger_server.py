"""Problem 07 (part A): messenger API server.

Task:
1. Create POST /messages endpoint, agree on the request schema with your partner
2. Print received message to server console
3. Return JSON confirmation (for example: {"status": "received"})
4. Share API with partner via ngrok (install it first: https://ngrok.com/)

Run:
    uvicorn 07_messenger_server:app --reload
    ngrok http 8000
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MessageIn(BaseModel):
    # TODO: add fields
    pass


@app.post("/messages")
def receive_message(payload: MessageIn) -> dict[str, str]:
    # TODO: print message details to console
    # TODO: return status response
    raise NotImplementedError
