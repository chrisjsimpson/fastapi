from app.core.config import settings
from fastapi import FastAPI

from app.api.api_v1.api import api_router

import urllib.request
import json

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json" # noqa
)


@app.get("/random", tags=["misc"])
async def random():
    from random import random
    return {"random_number": random()}

@app.get("/", tags=["misc"])
async def hello_world():
    return {"msg": "See /docs"}


@app.get("/xkcd", tags=["xkcd"])
async def xkcd_current():
    f = urllib.request.urlopen('http://xkcd.com/info.0.json')
    resp = f.read().decode('utf-8')
    return json.loads(resp)


@app.get("/xkcd/{comic_id}", tags=["xkcd"])
async def xkcd_comic(comic_id: int):
    f = urllib.request.urlopen('http://xkcd.com/info.0.json')
    resp = f.read().decode('utf-8')
    return json.loads(resp)

app.include_router(api_router, prefix=settings.API_V1_STR)
