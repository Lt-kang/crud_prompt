from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router import (
    posts,
    upload,
    submit
)

import os
import yaml
from pathlib import Path
with open(Path(__file__).parent / "config.yaml", "r") as f:
    config = yaml.safe_load(f)

SAVE_DIR = Path(config["SAVE_DIR"])
os.makedirs(SAVE_DIR, exist_ok=True)

UPSTAGE_SAVE_DIR = Path(config["UPSTAGE_SAVE_DIR"])
os.makedirs(UPSTAGE_SAVE_DIR, exist_ok=True)



app = FastAPI()

app.include_router(posts.router, prefix="/api/v1")
app.include_router(upload.router, prefix="/api/v1")
app.include_router(submit.router, prefix="/api/v1")


'''
get
/api/v1/inspect
/api/v1/extract


post
/api/v1/load
/api/v1/save
'''

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3020"],  # React 앱의 주소
    allow_origins=["*"],  # 모든 주소 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/api/health")
async def health_check():
    """API 상태 확인 엔드포인트"""
    return {"status": "healthy", "message": "FastAPI 서버가 정상 작동 중입니다"}


if __name__ == "__main__":
    uvicorn.run('run_api:app', host="localhost", port=8020, reload=True)

