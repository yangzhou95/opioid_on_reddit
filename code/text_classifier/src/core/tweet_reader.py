import pandas as pd
from core.tweet_cleaner import TweetCleaner
import csv

class TweetReader:

    def __init__(self, tweet_file, text_column='tweet', separator=',', encoding='latin1', header=None):
        self.corpus = []
        self.add_file_content_to_corpus(tweet_file, text_column, separator, encoding, header)

    def add_file_content_to_corpus(self,  tweet_file, text_column='tweet', separator=',', encoding='latin1', header=None):
        tweets_df = pd.read_csv(tweet_file, encoding=encoding, sep=separator, header=header, usecols=[text_column])
        all_tweets = tweets_df[text_column]
        for tweet in all_tweets:
            self.corpus.append(tweet)


    def get_corpus(self):
        return self.corpus

    # def get_tweets_df(self):
    #     return self.tweets_df

    def get_total_tweets(self):
        return len(self.get_corpus())

    def extract_words_frequency(self, num_words=None, min_threshold=None, stop_word_file='', ordered='desc'):

        my_clean_tweets = TweetCleaner.clean_text_data(self.corpus, stop_word_file)

        freq = {}

        for tweet in my_clean_tweets:
            words = tweet
            if isinstance(tweet, str):
                tweet = tweet.lower()
                words = tweet.split(' ')

            for word in words:
                count = freq.get(word, 0)
                freq[word] = count + 1

        frequency_list = freq.keys()
        results = []
        for word in frequency_list:
            if min_threshold is not None:
                if freq[word] < min_threshold:
                    continue
            tuple = (word, freq[word])
            results.append(tuple)

        byFreq = sorted(results, key=lambda word: word[1], reverse=True)

        if num_words is not None:
            byFreq = byFreq[: num_words]

        if ordered == 'asc':
            byFreq = sorted(byFreq, key=lambda word: word[1], reverse=False)

        return byFreq
