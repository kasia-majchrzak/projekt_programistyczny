import re
import gensim
from os import read
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class PreprocessingService:

    def preprocess_text(self, input_text: str) -> []:
        input_text = input_text.lower()
        input_text = re.sub('[^A-Za-z0-9\s]+', '', input_text)
        input_text_tokens = input_text.split(" ")

        vectorizer = TfidfVectorizer(stop_words='english')
        common_words = vectorizer.get_stop_words()
        if len(common_words) > 0:
            for word in common_words:
                if word in input_text_tokens:
                    input_text_tokens.remove(word)

        print(input_text_tokens)


    def tagged_document(self, list_of_list_of_words):
        for i, list_of_words in enumerate(list_of_list_of_words):
            yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])

        return list_of_list_of_words


    def compute_cosine_similarity(self, text1, text2):
        list_text = [text1, text2]

        vectorizer = TfidfVectorizer(stop_words='english')
        print(f'{vectorizer.get_stop_words()}')
        vectorizer.fit_transform(list_text)
        tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])
        cs_score = cosine_similarity(tfidf_text1, tfidf_text2)

        print(f'{np.round(cs_score[0][0], 2)}')

