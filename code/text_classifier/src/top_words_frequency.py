from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from core.tweet_reader import TweetReader
import statistics
import operator


reader = TweetReader('data/need/full-day-need/09_02.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_24.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_25.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_26.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_27.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_28.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_29.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_30.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/08_31.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/09_01.csv',  text_column=1, separator='|', encoding='utf8')
# reader.add_file_content_to_corpus('data/need/full-day-need/09_02.csv',  text_column=1, separator='|', encoding='utf8')

wfreq = reader.extract_words_frequency(num_words=None, min_threshold=None, stop_word_file='input/harvey_stopwords.txt', ordered='asc')

needs = TweetReader('/home/long/TTU-SOURCES/harvey-need/data/daily-need/needs.csv',  text_column=0, separator='|', encoding='utf8')
need_corpus = needs.get_corpus()

words_names = []
words_count = []

need_wfreq = dict()
frequencies = []
total_frequency = 0

for (word, freq) in wfreq:
    if word not in need_corpus:
        continue
    need_wfreq[word] = freq
    total_frequency += freq
    frequencies.append(freq)

median_freq = statistics.median(frequencies)
## remove low frequency items
final_wfreq = dict()
for word, freq in need_wfreq.items():
    if freq > median_freq:
        final_wfreq[word] = freq

sorted_wfreq = sorted(final_wfreq.items(), key=operator.itemgetter(1))
for word, freq in sorted_wfreq:
    words_names.append(word)
    words_count.append(freq)

print(final_wfreq)

show_plot = True

if show_plot == True:
    #
    fig, ax = plt.subplots()
    width = 0.56 # the width of the bars
    ind = np.arange(len(words_count))  # the x locations for the groups
    ax.barh(ind, words_count, width, color="blue")
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(words_names, minor=False)
    plt.title('Word Frequency')
    plt.xlabel('Frequencies')
    plt.ylabel('Words')
    for i, v in enumerate(words_count):
        ax.text(v + 0.2, i - .15, str(v), color='blue', fontweight='bold')
    plt.show()

