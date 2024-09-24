from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

Todo = []

class Item(BaseModel):
    id: int
    Name: str

@app.post("/todo")
def create_todo(todo: Item):
    Todo.append(todo)
    return todo

@app.get("/todo")
def get_todo():
    return Todo

@app.put("/todo/{id}")
def update_todo(todo: Item, id: int):
    for list in Todo:
        if (id == list.id):
            list.Name = todo.Name
            return list
    return {"message":"Error"}

@app.delete("/todo/{id}")
def delete_todo(id: int):
    for list in Todo:
        if (id == list.id):
            Todo.remove(list)
            return {"message":"Record Deleted !"}
    return {"message":"Error"}

