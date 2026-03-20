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
    pass


class TaskOut(BaseModel):
    # TODO: add id + task fields
    pass


# TODO: create in-memory storage and next_id counter


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> TaskOut:
    # TODO: create/store/return task
    raise NotImplementedError


@app.get("/tasks", response_model=list[TaskOut])
def get_tasks() -> list[TaskOut]:
    # TODO: return all tasks
    raise NotImplementedError
