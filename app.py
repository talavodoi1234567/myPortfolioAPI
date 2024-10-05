from typing import Union

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from data import *

app = FastAPI()
load_dotenv()

origins = [
    "http://localhost:3000",
    "https://react-learning-xpdu.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


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


class MessageSchema(BaseModel):
    name: str
    info: str
    subject: str
    message: str


@app.post("/send-message")
async def send_message(message: MessageSchema):
    message_text = f"""
New message from website:
Name: {message.name}
Info: {message.info}
Subject: {message.subject}
Message: {message.message}
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{TELEGRAM_API}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message_text}
        )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send message to Telegram")

    return {"status": "success", "message": "Message sent successfully"}