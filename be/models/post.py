from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Form


class gpt_model(BaseModel):
    model_name: str
    model_reasoning_effort: Optional[str] = Field(
        default=None,
        description="모델 추론 강도 선택: low, medium, high 중 하나",
        pattern="^(low|medium|high)?$"
    )
    user_prompt: str
    system_prompt: str
    image_path: Optional[str] = Field(
        default=None,
        description="image path",
    )
    table_path: Optional[str] = Field(
        default=None,
        description="table data(.xlsx, .csv) path",
    )
    pdf_path: Optional[str] = Field(
        default=None,
        description="pdf file path",
    )


class PostCreateForm(BaseModel):
    """Form 데이터 전용 모델"""
    # id: str = Form(...)
    # Form(...)은 FastAPI에서 라우트 핸들러 함수의 파라미터 타입 힌트에서 사용되어,
    # HTTP 요청에서 form 데이터(폼 데이터)로 해당 값을 추출해줍니다.
    # 하지만 Pydantic의 BaseModel 필드에서 직접 사용할 수는 없습니다.
    # BaseModel 모델에서는 그냥 타입 선언만 합니다:
    title: str
    date: str = Form(...)
    model: str = Form(...)
    prompt_tag: str = Form(...)
    prompt_content: str = Form(...)

    model: gpt_model = Form(...)
    
    class Config:
        # Form 데이터를 위한 설정
        json_schema_extra = {
            "example": {
                "id": "1756068834284",
                "title": "테스트 제목",
                "date": "2025-10-13",
                "model": "gpt-4",
                "prompt_tag": "분석",
                "prompt_content": "이미지를 분석해주세요"
            }
        }