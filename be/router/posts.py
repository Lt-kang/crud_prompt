from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from fastapi import Form

from pathlib import Path
import json
import zipfile
import io
from datetime import datetime
import pandas as pd
import yaml

with open(Path(__file__).parent.parent / "config.yaml", "r") as f:
    config = yaml.safe_load(f)

SAVE_DIR = Path(config["SAVE_DIR"])
UPSTAGE_SAVE_DIR = Path(config["UPSTAGE_SAVE_DIR"])


router = APIRouter()


@router.get("/posts", response_class=JSONResponse)
async def export_json(request: Request):
    posts_json_path = SAVE_DIR / "posts.json"
    if not posts_json_path.exists():
        with open(posts_json_path, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(posts_json_path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    # if posts == []:
    #     return JSONResponse(content=[], status_code=204)
    
    # return JSONResponse(content=posts, status_code=200)
    return posts


@router.get("/post/{id}", response_class=JSONResponse)
async def export_json(request: Request, id: str):
    post_json_path = SAVE_DIR / f"{int(id):04d}/info.json"

    with open(post_json_path, "r", encoding="utf-8") as f:
        post = json.load(f)


    return JSONResponse(content=post, status_code=200)