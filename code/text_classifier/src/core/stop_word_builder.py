from nltk.corpus import stopwords
from string import punctuation


class StopWordBuilder:
    def __init__(self, custom_stop_word_file):
        self.stopwords = StopWordBuilder._create_stop_words(custom_stop_word_file)

    @staticmethod
    def _create_stop_words(custom_stop_words):
        # remove common words and tokenize
        # list1 = ['RT', 'rt', 'get', 'got', 'would', 'think', 'thought', '"']
        my_stopwords = []
        with open(custom_stop_words) as f:
            for word in f:
                my_stopwords.append(word.rstrip('\n'))

        stop_list = stopwords.words('english') + list(punctuation) + my_stopwords

        return stop_list

    def get_stop_words(self):
        return self.stopwords
