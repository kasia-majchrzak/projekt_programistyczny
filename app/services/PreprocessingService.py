import re
from os import read


class PreprocessingService:
    COMMON_WORDS_PATH = "..\\..\\static\\txt\\commonWords.txt"

    def preprocess_text(self, input_text: str) -> []:
        input_text = input_text.lower()
        re.sub('[^A-Za-z0-9]+', '', input_text)
        input_text_tokens = input_text.split(" ")

        common_words_file = open(self.COMMON_WORDS_PATH).read()
        if len(common_words_file) > 0:
            for word in common_words_file.split(","):
                input_text_tokens = input_text_tokens.remove(word)

        return input_text_tokens

