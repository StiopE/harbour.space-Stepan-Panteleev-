"""Problem 06: POST -> GET tasks flow.

Task:
1. Keep in-memory task storage (dict or list)
2. Implement POST /tasks to add task with generated id
3. Implement GET /tasks to return all tasks
4. Verify: after POST, GET returns added task

Optional:
- Add GET /tasks/{task_id} with 404 for missing task
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class TaskIn(BaseModel):
    # TODO: add fields
    title: str
    completed: bool = False


class TaskOut(BaseModel):
    # TODO: add id + task fields
    id: int
    title: str
    completed: bool


# TODO: create in-memory storage and next_id counter
db: dict[int, TaskOut] = {}
next_id: int = 1

@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> TaskOut:
    # TODO: create/store/return task
    global next_id
    task = TaskOut(id=next_id, title= payload.title, completed=payload.completed)
    db[next_id] = task
    next_id +=1
    return task


@app.get("/tasks", response_model=list[TaskOut])
def get_tasks() -> list[TaskOut]:
    return list(db.values())


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int) -> TaskOut:
    if task_id not in db:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Task not found")
    return db[task_id]