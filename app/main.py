from fastapi import FastAPI, HTTPException
import urllib.request
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/random")
async def random():
    from random import random
    return {"random_number": random()}

@app.get("/xkcd")
async def xkcd_current():
    f = urllib.request.urlopen('http://xkcd.com/info.0.json')
    resp = f.read().decode('utf-8')
    return json.loads(resp)

@app.get("/xkcd/{commic_id}")
async def xkcd_current(commic_id: int):
    try:
        f = urllib.request.urlopen(f"http://xkcd.com/{commic_id}/info.0.json")
        resp = f.read().decode('utf-8')
        return json.loads(resp)
    except urllib.error.HTTPError:
        raise HTTPException(status_code=404, detail="Comic not found")

