##this is just for practice.on how i learnt what FASTAPI is. 

from fastapi import FastAPI,Path, Query
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class updateitem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None
@app.get("/")

def home():
    return{"data":"testing"}

@app.get("/about")

def about():
    return {"data":"about"}

"""inventory={
    1:{
        "name":"milk",
       "price":"3.99",
       "brand":"regular"
       }
}"""

inventory={}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(description="the id of the title youd like to view")):
    return inventory[item_id]

"""@app.get("/get-by-name")
def get_item(*,name:Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
    return{"data":"not found"}"""

@app.get("/get-by-name")
def get_item(*,name:Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id].name==name:
            return inventory[item_id]
    return{"data":"not found"}

"""@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:item):
    for item_id in inventory:
        return("error:'item id already exists'")
    inventory[item_id]={"name":item.name,"brand":item.brand,"price":item.price}
    return inventory[item_id]"""

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:updateitem):
    for item_id in inventory:
        return("error:'item id already exists'")
    inventory[item_id]=item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:updateitem):
    if item_id not in inventory:
        return{"error:item id doesnt exists"}
    if inventory.name!=None:
        inventory[item_id].name=item.name
    if inventory.price!=None:
        inventory[item_id].price=item.price
    if inventory.brand!=None:
        inventory[item_id].brand=item.brand   
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int=Query(...,description="the id of item to delete")):
    if item_id not in inventory:
        return{"error:item id doesnt exists"}
    del inventory[item_id]
