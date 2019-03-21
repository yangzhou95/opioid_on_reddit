#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:26:53 2018

@author: zhou
"""

# -*- coding: utf-8 -*-
"""
This module includes several functions that can be utilized to process text.
These functions are 
def remove_contractions(text): for example, it's --> it is, I'd --> I would
def remove_non_ascii(text):for example, remove emojis 
def to_lowercase(words):for example, convert text to lower case
def remove_punctuation(words): remove all the punctuations
def replace_numbers(words): for example, 321->three two one
def remove_stopwords(words): for example, remove words such as 'a', 'an', 'of', 'the'
def stem_words(words): for example, showers --> shower, improving --> improve
def lemmatize_verbs(words): am, is, are --> be, car, cars, car's, cars' --> car
def remove_number(words): for example, 2202 Mac Davis --> Mac Davis
def normalize(words):
def combine_word_list(list):
def prepare_data(fileName):
"""

import os
import re, string, unicodedata
import numpy as np
import pandas as pd

import json
import contractions
import nltk
import inflect

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

from pandas.io.json import json_normalize  # package for flattening json in pandas df

print(os.getcwd())
data_dir = 'your_data_dir'
os.chdir(data_dir)  # change to the dir where data is stored.


def remove_contractions(text):
    """remove contractions in string of text"""
    return contractions.fix(text)


def remove_non_ascii(text):
    """
    remove non-ASCII characters from list of tokenized words
    """
    words = nltk.word_tokenize(text)
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word). \
            encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def to_lowercase(words):
    """
    convert all characters to lowercase from a
    list of tokenized words
    """
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


def remove_punctuation(words):
    """
    remove punctuations
    """
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """
    convert integers in the list of tokenized words
    with textual representation
    """
    #    import inflect
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            #            print("digit "+new_word+"\n")
            new_words.append(new_word)
        else:
            #            print("word:" + word +"\n")
            new_words.append(word)
    return new_words


def remove_stopwords(words):
    """ remove stopwords """
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


def stem_words(words):
    """
    stem words in list of tokenized words
    """
    stemmer = nltk.stem.SnowballStemmer("english")
    #    stmmer = nltk.EnglishStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_verbs(words):
    """
    lemmatize verbs in lsit of tokenized words
    """
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def remove_number(words):
    """remove numbers"""
    new_words = []
    for word in words:
        if not word.isdigit():
            new_words.append(word)
    return new_words


def normalize(words):
    words = to_lowercase(words)
    words = remove_punctuation(words)
    #    words = replace_number(words)
    words = remove_stopwords(words)
    words = stem_words(words)
    words = lemmatize_verbs(words)
    return words


def process_a_row(text):
    text = remove_contractions(text)
    words = remove_non_ascii(text)
    words = remove_number(words)
    words = normalize(words)
    return words


def combine_word_list(list):
    text = ' '.join(list)
    return text

def prepare_data(fileName):
    df = pd.read_csv(fileName, header=None, names=['state', 'text', 'label'], usecols=[0, 1, 2])
    df["text1"] = df["text"].apply(process_a_row)
    df['text'] = df['text1'].apply(combine_word_list)
    return df

if __name__ == "__main__":

    file_test = "your_file.csv"
    file_train = "your_file.csv"

    df_train = prepare_data(file_train)
    df_test = prepare_data(file_test)
