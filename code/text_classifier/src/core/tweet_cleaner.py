from core.stop_word_builder import StopWordBuilder
import re


class TweetCleaner:
    def __init__(self, tweet_reader):
        self.tweetReader = tweet_reader


    @staticmethod
    def clean_text_data(text_array, stop_words_file=None):
        stop_builder = StopWordBuilder(stop_words_file)

        stop_list = stop_builder.get_stop_words()

        texts = [[word for word in re.findall('[a-z]{3,15}', str(document).lower()) if word not in stop_list] for document in text_array]

        return texts

    @staticmethod
    def clean_tweet(corpus, stop_word_file):
        return TweetCleaner.clean_text_data(corpus, stop_word_file)

    def clean_tweet_for_noun(self, corpus, stop_word_file):
        return []

    def clean_tweet_for_adjs_verbs(self, corpus, stop_word_file):
        return []

