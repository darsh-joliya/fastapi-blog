from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def index():
    return "Hello word"

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name":name, "price":price}


@app.put("/items/{item_id}")
def upd_item(item_id: int,name: str, price: float):
    return {"item_id":item_id, "name":name, "price":price}

@app.delete("/items/{item_id}")
def del_item(item_id: int):
    return {f"message : {item_id} Delete successfully "}