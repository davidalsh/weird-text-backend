from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

from src.utilities.encoder import Encoder

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


class TextObject(BaseModel):
    text: str


class EncoderResponse(BaseModel):
    encoded_text: str
    original_words: List[str]


@router.post("/encode", response_model=EncoderResponse)
def encode(text_instance: TextObject):
    encoder = Encoder(text_instance.text)
    encoded_text, original_words = encoder.to_weird_text()
    return {"encoded_text": encoded_text, "original_words": original_words}
