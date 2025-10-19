from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi import Form
from typing import List
from pathlib import Path
import json

import yaml
import os

with open(Path(__file__).parent.parent / "config.yaml", "r") as f:
    config = yaml.safe_load(f)

SAVE_DIR = Path(config["SAVE_DIR"])
UPSTAGE_SAVE_DIR = Path(config["UPSTAGE_SAVE_DIR"])
os.makedirs(SAVE_DIR, exist_ok=True)





router = APIRouter()





@router.post("/submit", response_class=JSONResponse)
async def save_json(
    id: str = Form(...),
    title: str = Form(...),
    date: str = Form(...),
    model: str = Form(...),
    prompt_tag: str = Form(...),
    prompt_content: str = Form(...),
    image_files: List[UploadFile] = File(...)
    # image_files: List[UploadFile] = File(...)
):
    """
    프론트엔드에서 아래와 같은 형태의 데이터를 POST로 보낸다고 가정:
    {
        "date": "2025-08-24",
        "id": 1756068834284,
        "image_files": [...],  # 파일 객체 배열 (프론트에서 실제 파일 업로드는 별도 처리 필요)
        "prompt_content": "...",
        "prompt_tag": "...",
        "title": "..."
    }
    """

    posts_json = Path(SAVE_DIR) / "posts.json"
    unit_save_path = Path(SAVE_DIR) / f"{int(id):04d}"
    os.makedirs(unit_save_path, exist_ok=True)

    local_img_paths = []
    for img_file in image_files:
        img_path = unit_save_path / img_file.filename
        with open(img_path, "wb") as f:
            content = await img_file.read()
            f.write(content)
        local_img_paths.append(img_path)

    with open(unit_save_path / "info.json", "w", encoding="utf-8") as f:
        json.dump({
            "id": id,
            "title": title,
            "date": date,
            "model": model,
            "prompt_tag": prompt_tag,
            "prompt_content": prompt_content,
            "result": [],
            "image_files": [img_file.filename for img_file in image_files],
        }, f, ensure_ascii=False, indent=2)

    posts_json = Path(SAVE_DIR) / "posts.json"
    with open(posts_json, "r", encoding="utf-8") as f:
        posts = json.load(f)
    posts.append({
        "date": date,
        "id": id,
        "title": title,
        "model": model,
        "prompt_tag": prompt_tag,
        "prompt_content": prompt_content,
        "api_call_completed": False
    })

    with open(posts_json, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)


    # _ocr = True if "OCR" in prompt_tag else False
    # for img_path in local_img_paths:
    #     result = api_call_action(img_path, model, _ocr=_ocr, prompt=prompt_content)


    return JSONResponse(content={"result": "success", "id": id})
