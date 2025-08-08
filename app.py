import asyncio
import os
import sqlite3

import httpx
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, HTTPException
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

'''async def send_webhook(url: str, payload: dict):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()


async def analyze_then_notify(webhook_url: str, message: str):
    result = await analyze_dream(message=message)
    await send_webhook(webhook_url, {"event": "dream-analyzed", "data": result})


@app.post("/dream")
async def ai_response(payload: dict, tasks: BackgroundTasks):
    webhook_url = payload.get("webhook_url")
    if not webhook_url:
        raise HTTPException(400, detail="Missing webhook_url")

    message = payload.get("message", "")

    # 1) Notify immediately that we started (non-blocking)
    tasks.add_task(send_webhook, webhook_url, {
                   "event": "received", "received": True})

    # 2) Kick off analysis; result will be posted later (non-blocking)
    tasks.add_task(analyze_then_notify, webhook_url, message)

    # 3) Return right away
    return JSONResponse(status_code=202, content={"status": "processing"})'''
