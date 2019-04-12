import os
import re

import pandas as pd
import numpy as np

import json

from pandas.io.json import json_normalize

def deidentificate(userid):
    userid = 'voluntold123'

filename = "reddit_0samaBinNoddin.json"
patterns = re.compile(r'(reddit_)(.+)(\.json)')
match_result = patterns.match(filename)
username = match_result.groups()[1]

print('username: ', username)

data = None
container_list = None

with open(filename, 'r') as f:
    data = json.load(f)
    csv2 = ""
    for author, post_content in data.items(): # post_content is a list

        # print('author: ', author)
        # print('post_content: ', post_content) # post_content is a list
        post_dict = post_content[0] # it's a dict
        for post_comment in post_dict:
            # print("post_dict: ", post_comment)
            comment_list = post_dict[post_comment] # it's a list
            print(comment_list)
            for comment_dict in comment_list:
                for comment_id in comment_dict:
                    comment_content_list = comment_dict[comment_id]
                    for comment_content_dict in comment_content_list:
                        print(comment_content_dict)
                        for key in comment_content_dict:
                            print(key)

                            try:
                                text = comment_content_dict[key]
                            except KeyError:
                                pass
                            print(text)
                            patterns_author =