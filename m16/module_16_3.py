from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

msg_db = {"0": "First post in FastApi"}

@app.get("/")
async def get_all_msgs() -> dict:
    return msg_db

@app.get("/msg/{msg_id}")
async def get_msg(msg_id: str) -> dict:
    return msg_db[msg_id]

@app.post("/msg")
async def create_msg(msg: str) -> str:
    current_index = str(int(max(msg_db, key=int))+1)
    msg_db[current_index] = msg
    return msg
@app.put("/msg/{msg_id}")
async def update_msg(msg_id: str, msg: str) -> str:
    msg_db[msg_id] = msg
    return "Msg updated"
@app.delete("/msg/{msg_id}")
async def delete_msg(msg_id: str) -> str:
    msg_db.pop(msg_id)
    return f"Message with {msg_id} was deleted"

@app.delete("/")
async def del_all_msgs() -> str:
    msg_db.clear()
    return "All messages was deleted"
