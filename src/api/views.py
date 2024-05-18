from typing import Dict
from fastapi import APIRouter
from pydantic import BaseModel

from src.utilities.decoder import Decoder
from src.utilities.encoder import Encoder

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


class TextObject(BaseModel):
    text: str


@router.post("/encode", response_model=Dict[str, str])
def encode(text_instance: TextObject):
    encoder = Encoder(text_instance.text)
    encoded_text = encoder.get_weird_text()
    return {"text": encoded_text}


@router.post("/decode", response_model=Dict[str, str])
def decode(text_instance: TextObject):
    decoder = Decoder(text_instance.text)
    decoded_text = decoder.get_original_text()
    return {"text": decoded_text}
