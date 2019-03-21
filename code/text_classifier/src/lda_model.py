from mmap import mmap

from gensim import corpora, models, similarities
from gensim import corpora
from collections import OrderedDict
import pandas as pd

#visualization package
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import pyLDAvis.gensim


def create_lda_model(corpus_file, dict_file, num_topics=5):
    dictionary = corpora.Dictionary.load(dict_file)
    corpus = corpora.MmCorpus(corpus_file)

    tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
    corpus_tfidf = tfidf[corpus]  # step 2 -- use the model to transform vectors

    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topics)
    corpus_lda = lda[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

    return lda, corpus_lda, dictionary, num_topics


fileName = 'opioid-pos'
mm_corpus_file = 'output/' + fileName + '.mm'
mm_dict_file = 'output/' + fileName + '.dict'
NUM_WORDS = 5
TOTAL_TOPICS = 2

lda, corpus_lda, dictionary, total_topics = create_lda_model(corpus_file=mm_corpus_file, dict_file=mm_dict_file, num_topics=TOTAL_TOPICS)

# Show first n important word in the topics:
topic_words = lda.show_topics(total_topics, num_words=NUM_WORDS)

print(topic_words)

data_lda = {i: OrderedDict(lda.show_topic(i, 25)) for i in range(total_topics)}
df_lda = pd.DataFrame(data_lda)
df_lda = df_lda.fillna(0).T

g = sns.clustermap(df_lda.corr(), center=0, cmap="RdBu", metric='cosine', linewidths=.75, figsize=(12, 12))
plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.show()
#plt.setp(ax_heatmap.get_yticklabels(), rotation=0)  # For y axis

# pyLDAvis.s
# pyLDAvis.enable_notebook()
# panel = pyLDAvis.gensim.prepare(lda, corpus_lda, dictionary, mds='tsne')

# prepare LDA_topics model visualization
LDA_vis_data = pyLDAvis.gensim.prepare(lda, corpus_lda, dictionary)
# save visualization
pyLDAvis.save_html(LDA_vis_data, 'output/vis/' + fileName + '-topic.html')
