import re
import nltk
from nltk import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_text(input_text: str) -> []:
    input_text = re.sub('[^A-Za-z0-9\s]+', '', input_text)
    input_text_tokens = word_tokenize(input_text)
    input_text_tokens = stemSentence(input_text_tokens)
    input_text_tokens = lemmatizeSentence(input_text_tokens)

    vectorizer = TfidfVectorizer(stop_words='english')
    common_words = vectorizer.get_stop_words()
    if len(common_words) > 0:
        for word in common_words:
            if word in input_text_tokens:
                input_text_tokens = [value for value in input_text_tokens if value != word]

    return input_text_tokens


def stemSentence(token_words):
    porter = PorterStemmer()
    #lancaster = LancasterStemmer()
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))

    return stem_sentence


def lemmatizeSentence(token_words):
    wordnet_lemmatizer = WordNetLemmatizer()

    for word in token_words:
        word = wordnet_lemmatizer.lemmatize(word, pos="v")

    return token_words
