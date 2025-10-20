from fastapi import (
    APIRouter, Request, Form, UploadFile, File, Depends, HTTPException
)
from fastapi.responses import JSONResponse

from typing import Annotated, Optional
import json


from models.submit import PostCreateForm
from pydantic import ValidationError



def parsing_form(post_create_form: Annotated[str, Form(...)]) -> PostCreateForm:
    try:
        # JSON 파싱 + 스키마 검증
        return PostCreateForm.model_validate_json(post_create_form)

    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())






router = APIRouter()

@router.post("/submit")
async def save_json(
    post_create_form: Annotated[PostCreateForm, Depends(parsing_form)],
    image_file: Optional[UploadFile] = File(None),
    table_file: Optional[UploadFile] = File(None),
    pdf_file:   Optional[UploadFile] = File(None),
):

    print(post_create_form)
    if image_file:
        print("V")
        print(image_file)
    if table_file:
        print(table_file)
    if pdf_file:
        print(pdf_file)
    # 각종 파일 save_dir에 저장
    # model_info.model_name에 맞게 model에 api 요청
    # 입력 결과 DB 저장
    # 출력 결과 DB 저장

    return JSONResponse(content={"result": "success"})
