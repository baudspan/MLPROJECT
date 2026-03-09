from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

topics={}
counter=1

class Topic(BaseModel):
    name:str
    category:str
    done:bool=False

@app.post("/topics",status_code=201)
def add_topic(topic:Topic):
    global counter 
    topics[counter]=topic
    counter+=1
    return topics[counter-1]
    
@app.get("/get-topics/{id}")
def get_topics(id:int):
    if id not in topics:
        raise HTTPException(status_code=404)
    return topics[id]

@app.put("/topics/{id}")
def mark_done(id:int):
    if id not in topics:
        raise HTTPException(status_code=404)
    topics[id].done=True
    return topics[id]

@app.delete("/topics/{id}")
def delete_topics(id:int):
    topics.pop(id)
    if id not in topics:
        raise HTTPException(status_code=404)
    return{"message":"deleted"}