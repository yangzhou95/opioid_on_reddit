from core.text_to_number import TextToNumber
import pandas as pd


textToNumber = TextToNumber()
df = pd.read_csv('data/output.csv')

body_raw = df['body'].tolist()
title_raw = df['issue_title'].tolist()
#preview output of first element

train_body_raw = body_raw[0:1000]
train_title_raw = body_raw[0:1000]


train_body_vecs = textToNumber.create_number_vector(train_body_raw, output_file='output/seq2seq/body')
train_title_vecs = textToNumber.create_number_vector(train_title_raw, output_file='output/seq2seq/title')


print('done')
