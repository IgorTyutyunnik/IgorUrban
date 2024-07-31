from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
def all_task():
    pass


@router.get("/task_id")
def task_by_id():
    pass


@router.post("/create")
async def creaty_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass
