from fastapi import FastAPI, HTTPException
from typing import List
from stack import Stack
from queue import Queue

app = FastAPI()

stack = Stack()
queue = Queue()

@app.get("/stack/")
def read_stack():
    return {"stack": stack.__print__()}

@app.post("/stack/")
def add_to_stack(item: int):
    stack.push(item)
    return {"item": item}

@app.delete("/stack/{item_id}")
def remove_from_stack(item_id: int):
    try:
        stack.pop()
        return {"item_id": item_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/queue/")
def read_queue():
    return {"queue": queue.__print__()}

@app.post("/queue/")
def add_to_queue(item: int):
    queue.enqueue(item)
    return {"item": item}

@app.delete("/queue/{item_id}")
def remove_from_queue(item_id: int):
    try:
        queue.dequeue()
        return {"item_id": item_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
