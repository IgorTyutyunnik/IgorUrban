from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
async def get_dict():
    return users

@app.post("/user/{username}/{age}")
async def post_users(user: User, username: str, age: int):
    user_id = len(users) + 1
    user = [user_id, username, age]
    users.append(user)
    return  f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def put_users(user_id: int, username: str, age: int):
    try:
        user_apd = users[user_id-1]
        user_apd[1] = username
        user_apd[2] = age
        return f"User {user_id} is registered"
    except:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        users.pop(user_id-1)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
