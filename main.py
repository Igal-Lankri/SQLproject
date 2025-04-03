from fastapi import FastAPI, Request
from db import insert_log, get_logs

app = FastAPI()

@app.post("/logs")
async def create_log(request: Request):
    body = await request.json()
    message = body.get("message")
    if not message:
        return {"error": "Message required"}
    insert_log(message)
    return {"status": "Log saved"}

@app.get("/logs")
def read_logs():
    return get_logs()

