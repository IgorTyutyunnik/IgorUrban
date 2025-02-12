from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
def all_users():
    pass


@router.get("/user_id")
def user_by_id():
    pass


@router.post("/create")
async def creaty_user():
    pass


@router.put("/update")
async def update_user():
    pass


@router.delete("/delete")
async def delete_user():
    pass
