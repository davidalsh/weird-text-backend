from typing import Dict
from fastapi import APIRouter
from pydantic import BaseModel

from src.utilities.encoder import Encoder

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


class TextObject(BaseModel):
    text: str


@router.post("/encode", response_model=Dict[str, str])
def encode(text_instance: TextObject):
    encoder = Encoder(text_instance.text)
    encoded_text = encoder.to_weird_text()
    return {"text": encoded_text}
