import base64  
import json
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

# gpt api
from openai import AsyncOpenAI

async def gpt_api_call(
    user_prompt:str,
    system_prompt:str,
    
    model:gpt_model,

    image_path:str = None,

):
    
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    system_role = {
        "role": "system",
        "content": [
            { 
                "type": "input_text", 
                "text": system_prompt 
            },
        ],
    }

    user_role = {
            "role": "user",
            "content": [
                { 
                    "type": "input_text", 
                    "text": user_prompt 
                }
            ]
        }


    if image_path is not None:
        base64_image = encode_image(image_path)
        user_role["content"].append({
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
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

