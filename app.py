from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import *

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/familiarwith")
async def familiarWithAPI():
    return {
        'familiarWith': getFamiliarWith()
    }


@app.get('/header/{language}')
async def getHeaderAPI(language):
    return {
        'header': getHeader(language)
    }

@app.get('/overall')
async def getOverall():
    return overAllData()