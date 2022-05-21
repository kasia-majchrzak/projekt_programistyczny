from .PreprocessingService import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class TextSimilarityService:

    def __init__(self, text1: str, text2: str):
        self._tokens1 = preprocess_text(text1)
        self._tokens2 = preprocess_text(text2)
        self._all_tokens = list(set(self._tokens1) | set(self._tokens2))
        self._all_texts = [text1, text2]

    def calculate_similarity(self):
        Tfidf_vect = TfidfVectorizer()
        vector_matrix = Tfidf_vect.fit_transform(self._all_texts)
        cosine_similarity_matrix = cosine_similarity(vector_matrix)
        return cosine_similarity_matrix[0, 1] * 100

    def get_bow(self, tokens):
        tf_diz = dict.fromkeys(self._all_tokens, 0)
        for word in self._all_tokens:
            tf_diz[word] = tokens.count(word)
        return tf_diz



