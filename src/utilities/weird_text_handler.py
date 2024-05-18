from src.utilities import constants
from typing import List
import re


class WeirdTextHandler:
    """
    Base class for handling text encoding and decoding with 'weird' text transformations.
    """

    word_pattern = constants.WORD_PATTERN
    weird_separator = constants.WEIRD_SEPARATOR

    def __init__(self, text: str = ""):
        self.text = text

    def _get_text_words(self) -> List[str]:
        """Extracts words from the text using the word pattern."""
        return re.findall(self.word_pattern, self.text)
