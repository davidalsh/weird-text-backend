import re
from typing import Tuple, List
from itertools import permutations
from src.utilities.constants import WORD_PATTERN, WEIRD_SEPARATOR


def check_word(original_word: str, weird_word: str) -> Tuple[bool, bool]:
    """
    Verifies if 'weird' word was based on original word

    Args:
        original_word: original word from text.
        weird_word: encrypted word by weird Encoder.

    Returns:
        - The first boolean indicates if the weird word was based on original word.
        - The second boolean indicates if the original word should be added to the changed words list.
    """

    if len(original_word) != len(weird_word):
        return False, False
    if len(original_word) == 1:
        return original_word == weird_word, False
    if original_word[0] != weird_word[0] or original_word[-1] != weird_word[-1]:
        return False, False

    weird_word_inner_part = weird_word[1:-1]
    if original_word == weird_word:
        if len(original_word) in [2, 3]:
            return True, False
        if len(set(weird_word_inner_part)) == 1:
            return True, False
        return False, False

    weird_word_inner_part_permutations = ["".join(char_perm) for char_perm in permutations(weird_word_inner_part)]
    return original_word[1:-1] in weird_word_inner_part_permutations, True


class WeirdWordTestBase:
    """
    Base class for handling testing text encoding and decoding with 'weird' text transformations.
    """

    def __init__(self, weird_data_json: dict, original_data_json: dict):
        self.weird_data_json = weird_data_json
        self.original_data_json = original_data_json
        self.original_words = self._get_original_words()
        self.weird_text = ""
        self.weird_data_original_changed_words_list = []
        self.original_changed_words_list = []
        self.weird_words = []
        self._parse_weird_data_json()

    def _get_original_words(self) -> List[str]:
        """Extracts words from the text using the word pattern."""
        return re.findall(WORD_PATTERN, self.original_data_json["text"])

    def _parse_weird_data_json(self):
        """Extracts weird text, changed words list from weird data
        and updates weird words."""
        json_text_split = self.weird_data_json.get("text", "").split(WEIRD_SEPARATOR)
        assert len(json_text_split) == 3
        assert not json_text_split[0]
        self.weird_text = json_text_split[1]
        self.weird_data_original_changed_words_list = json_text_split[2].split()
        self.weird_words = re.findall(WORD_PATTERN, self.weird_text)

    def check_words(self):
        """Checks if weird word is based on original word."""
        for original_word, weird_word in zip(self.original_words, self.weird_words):
            is_from_original, is_changed = check_word(original_word, weird_word)
            assert is_from_original
            if is_changed:
                self.original_changed_words_list.append(original_word)

    def check_original_words(self):
        """Checks if weird changed words are the same as original changed words"""
        assert sorted(self.original_changed_words_list) == self.weird_data_original_changed_words_list

    def process(self):
        self.check_words()
        self.check_original_words()
