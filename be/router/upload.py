from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Form


from pathlib import Path
import json
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=str(Path(__file__).parent.parent / ".env"))
SAVE_DIR = os.getenv("SAVE_DIR")
UPSTAGE_SAVE_DIR = os.getenv("UPSTAGE_SAVE_DIR")



router = APIRouter()



@router.post("/load", response_class=JSONResponse)
async def load_file(
    request: Request,
    file: UploadFile = File(...),
    data: str = Form(...)
):
    ...

    '''
    data["call_type"] 읽어서 OCR이 있을 경우
    모든 image파일을 일단 upstage에 올려서
    '''
