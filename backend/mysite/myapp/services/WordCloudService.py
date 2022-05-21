from .PreprocessingService import preprocess_text
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class WordCloudService:

    def __init__(self, text: str):
        self._tokens = preprocess_text(text)

    def generate_word_cloud(self):
        bow = self.get_bow()
        cloud = WordCloud(max_words=100)
        cloud.generate_from_frequencies(bow)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis("off")
        cloud.to_file("wordcloud.jpg")
        file_obj = open("wordcloud.jpg", mode="rb")
        return file_obj

    def get_bow(self):
        tf_diz = dict.fromkeys(self._tokens, 0)
        for word in self._tokens:
            tf_diz[word] = self._tokens.count(word)
        return tf_diz
