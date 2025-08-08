import os
import sqlite3
from re import M

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from open_ai_call import analyze_dream

load_dotenv()
app = FastAPI()


@app.post("/dream")
async def ai_response(
    message: str
):
    result = await analyze_dream(message=message)
    return JSONResponse(content=result)
