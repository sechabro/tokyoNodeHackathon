# import httpx
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import JSONResponse
#
# app = FastAPI()
#
# SERVER_URL = "http://localhost:8000/dream"
# WEBHOOK_URL = "http://localhost:9000/hook/dream"
#
#
# @app.post("/hook/dream")
# async def dream_analysis_notification(payload: dict):
#    # This simulates the client's webhook receiver
#    print("WEBHOOK HIT:", payload)
#    return JSONResponse(content={"ok": True, "got": payload})
#
#
# @app.post("/send-dream")
# async def send_dream(payload: dict):
#    # Inject the webhook URL so the server knows where to call back
#    payload = {**payload, "webhook_url": WEBHOOK_URL}
#    async with httpx.AsyncClient(timeout=10) as client:
#        r = await client.post(SERVER_URL, json=payload)
#        if r.status_code >= 400:
#            raise HTTPException(502, detail="failed to send dream away...")
#        return JSONResponse(content={"server_response": r.json()})
