from core.tweet_reader import TweetReader
import statistics
import operator
import matplotlib.pyplot as plt
import numpy as np

reader = TweetReader('data/texasfarmbureau/2017-06.csv',  text_column="text", separator=',', header=0)
wfreq = reader.extract_words_frequency(num_words=None, min_threshold=None, stop_word_file='input/farmers_stop_words.txt', ordered='asc')

words_names = []
words_count = []

need_wfreq = dict()
frequencies = []
total_frequency = 0

for (word, freq) in wfreq:
    need_wfreq[word] = freq
    total_frequency += freq
    frequencies.append(freq)

median_freq = statistics.median(frequencies)
median_freq = 4
## remove low frequency items
final_wfreq = dict()
for word, freq in need_wfreq.items():
    if freq > median_freq:
        final_wfreq[word] = freq

sorted_wfreq = sorted(final_wfreq.items(), key=operator.itemgetter(1))
for word, freq in sorted_wfreq:
    words_names.append(word)
    words_count.append(freq)

print(sorted_wfreq)

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

