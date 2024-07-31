from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
def get_dict(request: Request, user_id: int) -> HTMLResponse:
    try:
        user = [user_id, users[user_id - 1][0], users[user_id - 1][1]]
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def post_users(user: User, username: str, age: int):
    user = [username, age]
    users.append(user)
    user_id = len(users)
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def put_users(user_id: int, username: str, age: int):
    try:
        user = users[user_id - 1]
        user = [username, age]
        users[user_id - 1] = user
        return f"User {user_id} is registered"
    except:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    try:
        users.pop(user_id - 1)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
