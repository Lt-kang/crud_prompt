import base64  
import json
import pandas as pd
from fastapi import HTTPException
from models.submit import ModelInfo


import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def encode_file(file_path):
    with open(file_path, "rb") as file:
        return file

# gpt api
from openai import AsyncOpenAI

async def gpt_api_call(
    model: ModelInfo,

    image_path:str = None,
    table_path:str = None,
    pdf_path:str = None,

):
    
    try:
        client = AsyncOpenAI(api_key=model.api_key)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API 키 오류: {e}") from e

    system_role = {
        "role": "system",
        "content": [
            { 
                "type": "input_text", 
                "text": model.system_prompt 
            },
        ],
    }

    user_role = {
            "role": "user",
            "content": [
                { 
                    "type": "input_text", 
                    "text": model.user_prompt 
                }
            ]
        }


    if image_path is not None:
        base64_image = encode_image(image_path)
        user_role["content"].append({
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    })

    if table_path is not None:
        file = await client.files.create(
                                        file=open(table_path, "rb"),
                                        purpose="user_data",
                                    )
        user_role["content"].append({
            "type": "input_file",
            "file_id": file.id
        })

    if pdf_path is not None:
        file = await client.files.create(
                                        file=open(pdf_path, "rb"),
                                        purpose="user_data",
                                    )
        user_role["content"].append({
            "type": "input_file",
            "file_id": file.id
        })

    input_form = {
        "model": model.model_name,
        "input": [
            system_role,
            user_role
        ]
    }

    if model.model_reasoning_effort is not None:
        input_form["reasoning_effort"] = model.model_reasoning_effort

    response = await client.responses.create(
        **input_form
    )


    response_json = response.model_dump_json() # str
    res_json = json.loads(response_json)

    return res_json

