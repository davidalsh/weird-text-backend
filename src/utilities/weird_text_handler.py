from src.utilities import constants
from typing import List
import re


class WeirdTextHandler:
    word_pattern = constants.WORD_PATTERN
    weird_separator = constants.WEIRD_SEPARATOR

    def __init__(self, text):
        self.text = text

    def _get_text_words(self) -> List[str]:
        return re.findall(self.word_pattern, self.text)
