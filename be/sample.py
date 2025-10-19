from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from slack_sdk import WebClient
from pathlib import Path
import os
import json
import uvicorn

from datetime import datetime
import logging
logging.basicConfig(
    level=logging.INFO,    
    format="%(asctime)s [%(levelname)s] %(message)s",  # 로그 포맷
    datefmt="%Y-%m-%d %H:%M:%S",                 # 시간 포맷
    handlers=[
        logging.FileHandler(f"slack-bot_server_{datetime.now().strftime('%Y-%m-%d')}.log", encoding='utf-8'),  # 파일로 저장
    ]
)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

app = FastAPI()
slack = WebClient(token=SLACK_BOT_TOKEN)

class NotifyRequest(BaseModel):
    user_name: str
    message: str






@app.post("/notify")
async def notify(req: NotifyRequest, request: Request):
    client_ip = request.client.host
    log_message = f'''User Name: {req.user_name}  IP: {client_ip}  Message: {req.message}'''

    user_id_mapping = json.loads((Path(__file__).parent / "user_mapping.json").read_text(encoding="utf-8"))

    try:
        slack.chat_postMessage(channel=user_id_mapping[req.user_name], text=req.message)
        slack.chat_postMessage(channel=user_id_mapping["강승현"], text=req.message)
        logger.info(log_message)
        return JSONResponse(
            status_code=200,
            content={"status": "ok"}
            )

    except Exception as e:
        error_message = f'''{log_message}  Error: {str(e)}'''

        logger.exception(error_message)
        slack.chat_postMessage(channel=user_id_mapping["강승현"], text=error_message)
        return JSONResponse(
            status_code=500,
            content={"status": "error"}
            )


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="172.127.0.201", port=7501, reload=True)