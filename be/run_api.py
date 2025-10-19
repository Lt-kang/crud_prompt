from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router import (
    posts,
    upload,
    submit
)


import os
from dotenv import load_dotenv
load_dotenv()
DEV = os.getenv("DEV") == "True"

'''
logging
'''
if DEV:
    print("======================================")
    print("===============DEV_MODE===============")
    print("==============NO LOGGING==============")
    print("======================================")

else:
    import logging
    import datetime

    logging.basicConfig(
        level=logging.INFO,    
        format="%(asctime)s [%(levelname)s] %(message)s",  # 로그 포맷
        datefmt="%Y-%m-%d %H:%M:%S",                 # 시간 포맷
        handlers=[
            logging.FileHandler(f"slack-bot_server_{datetime.now().strftime('%Y-%m-%d')}.log", encoding='utf-8'),  # 파일로 저장
        ]
    )
    logger = logging.getLogger(__name__)





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
    if DEV:
        uvicorn.run('run_api:app', host="localhost", port=8020, reload=True)
    else:
        uvicorn.run('run_api:app', host="localhost", port=8020)


