from typing import Union
from fastapi import FastAPI, HTTPException
from amazeme import generate_gift_ideas
MAX_INPUT_LENGTH = 25

app = FastAPI()


@app.get("/generate_gift_ideas")
async def generate_gift_ideas_api(prompt1: str, prompt2: str, prompt3: str):
    Validate_length_1(prompt1)
    Validate_length_2(prompt2)
    Validate_length_3(prompt3)
    ideas = generate_gift_ideas(prompt1, prompt2, prompt3)
    return {"ideas": ideas}


def Validate_length_1(prompt1: str):
    if len(prompt1) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} char")


def Validate_length_2(prompt2: str):
    if len(prompt2) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} char")


def Validate_length_3(prompt3: str):
    if len(prompt3) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} char")

# uvicorn amazeme_api:app --reload
