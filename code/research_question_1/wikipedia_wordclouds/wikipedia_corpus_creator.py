from email import contentmanager
import requests
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

class WikiCorpusCreator:
    api_path = 'https://de.wikipedia.org/w//api.php?format=xml&action=query&prop=extracts&titles={}&redirects=true'

    def __init__(self,topic, exclude_stopwords = False, stopwords_file = None, max_amount_of_words = None):
        self.wordcloud = None

        if exclude_stopwords:
            if stopwords_file is None:
                self.stopwords = self._create_stopwords_list("german_stopwords.txt")
            else:
                self.stopwords = self._create_stopwords_list(stopwords_file)
            
            STOPWORDS.update(self.stopwords)

        self.current_path = self.api_path.format(topic)
        self.text = self._get_wikipedia_text()
        self.clean_text = self._get_clean_text(self.text)
        self.cap_words = self._get_capital_letter_words_as_string(self.clean_text)
        self.wordcloud = self._generate_wordcloud(self.cap_words, max_amount_of_words)

    def get_text(self):
        return self.text
    
    def get_corpus(self):
        return self.wordcloud.words_.keys()
    
    def draw_wordcloud(self):
        plt.imshow(self.wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def _create_stopwords_list(self, file):
        my_file = open(file, "r")
        content = my_file.read()
        my_file.close()

        content_list = content.split("\n")

        return content_list
    
    def _generate_wordcloud(self, text, amount = None):
        if amount != None:
            return WordCloud(background_color='white', max_words = amount).generate(text) 

        return WordCloud(background_color='white').generate(text)

    def _get_wikipedia_text(self):
        response = requests.get(self.current_path, 
                                params = {
                                    'action': 'query',
                                    'format': 'json',
                                    'prop': 'extracts',
                                    'explaintext': True,
                                }).json()
        page = next(iter(response['query']['pages'].values()))
        text = page['extract']

        return text

    def _get_clean_text(self, text):
        return re.sub(r'[^\w]',' ',text)
    
    def _get_capital_letter_words_as_string(self, text):
        capital_letter_words = self._get_capital_letter_words(text)
    
        return ' '.join(map(str, capital_letter_words))
    
    def _get_capital_letter_words(self, text):
            return re.findall(r'[A-ZÄÖÜ][0-9A-ZÄÖÜa-zäöüß]+',text)
    

 
