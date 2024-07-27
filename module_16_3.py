from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_dict():
    return users

@app.post("/user/{username}/{age}")
async def post_users(username: str, age: int):
    user_id = str(int(max(users, key= int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return  f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def put_users(user_id: str, username: str, age: int):
    users[user_id] =f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.delete("/user/{user_id}")
async def username(user_id: str):
    users.pop(user_id)
    return f"User {user_id} has been deleted"