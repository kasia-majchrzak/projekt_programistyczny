import nltk
from .PreprocessingService import preprocess_text
import heapq
import re


class TextSummaryService:

    def __init__(self, text: str):
        self._text = text
        self._text = re.sub(r'[[0-9]*]', ' ', self._text)
        self._text = re.sub(r'\s+', ' ', self._text)
        self._formatted_text = re.sub('[^a-zA-Z]', ' ', self._text)
        self._formatted_text = re.sub(r'\s+', ' ', self._formatted_text)
        self._tokens = nltk.sent_tokenize(text)

    def get_text_summary(self) -> str:
        word_freq = self.get_frequencies()
        sentence_scores = self.get_sentence_scores(word_freq)
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    def get_frequencies(self):
        stopwords = nltk.corpus.stopwords.words('english')
        word_frequencies = {}
        for word in nltk.word_tokenize(self._formatted_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        max_freq = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / max_freq)

        return word_frequencies

    def get_sentence_scores(self, word_frequencies):
        sentence_scores = {}
        for sent in self._tokens:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        return sentence_scores

