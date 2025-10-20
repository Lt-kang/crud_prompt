from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Form
from datetime import datetime
import uuid




class PostData(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="고유ID / 자동입력 / (UUID4)",
    )
    title: str = Field(
        default="",
        description="제목을 입력합니다.",
        min_length=1,
        max_length=100,
    )
    author: str = Field(
        default="",
        description="작성자를 입력합니다.",
        min_length=1,
        max_length=100,
    )
    create_at: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        description="작성일 / 자동입력 / (YYYY-MM-DD HH:MM:SS)",
    )



class ModelInfo(BaseModel):
    model_name: str
    model_reasoning_effort: Optional[str] = Field(
        default=None,
        description="모델 추론 강도 선택: low, medium, high 중 하나",
        pattern="^(minimal|low|medium|high)?$"
    )
    user_prompt: str
    system_prompt: str
    api_key: str
    # image_path: Optional[str] = Field(
    #     default=None,
    #     description="image path",
    # )
    # table_path: Optional[str] = Field(
    #     default=None,
    #     description="table data(.xlsx, .csv) path",
    # )
    # pdf_path: Optional[str] = Field(
    #     default=None,
    #     description="pdf file path",
    # )


class PostCreateForm(BaseModel):
    post_data: PostData
    model_info: ModelInfo
    

    
    # class Config:
    #     # Form 데이터를 위한 설정
    #     json_schema_extra = {
    #         "example": {
    #             "id": "1756068834284",
    #             "title": "테스트 제목",
    #             "date": "2025-10-13",
    #             "model": "gpt-4",
    #             "prompt_tag": "분석",
    #             "prompt_content": "이미지를 분석해주세요"
    #         }
    #     }