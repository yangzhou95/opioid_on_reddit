
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path

np.random.seed(19680801)
data = np.random.randn(1000)
# plt.hist(data, bins='auto')
plt.hist(data, bins=5)
plt.title("Histogram with 'auto' bins")
plt.show()
#
# fig, ax = plt.subplots()
#
# # Fixing random state for reproducibility
# # np.random.seed(19680801)
#
#
# # histogram our data with numpy
#
# # data = np.random.randn(1000)
# n, bins = np.histogram(data, 5)
#
# # get the corners of the rectangles for the histogram
# left = np.array(bins[:-1])
# right = np.array(bins[1:])
# bottom = np.zeros(len(left))
# top = bottom + n
#
#
# # we need a (numrects x numsides x 2) numpy array for the path helper
# # function to build a compound path
# XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
#
# # get the Path object
# barpath = path.Path.make_compound_path_from_polys(XY)
#
# # make a patch out of it
# patch = patches.PathPatch(barpath)
# ax.add_patch(patch)
#
# # update the view limits
# ax.set_xlim(left[0], right[-1])
# ax.set_ylim(bottom.min(), top.max())
#
# plt.show()

# import os
# import numpy as np
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# import plotly as py
# import plotly.graph_objs as go
#
# # init_notebook_mode(connected=True) #do not miss this line
#
# from gensim import corpora, models, similarities
#
# import warnings
# import pandas as pd
#
# warnings.filterwarnings("ignore")
#
#
# datafile = 'input/data_elonmusk.csv'
#
# tweets = pd.read_csv(datafile, encoding='latin1')
# tweets = tweets.assign(Time=pd.to_datetime(tweets.Time)).drop('row ID', axis='columns')
#
# tweets.head(10)
#
# range(len(tweets['Tweet']))
# tweets['Time'] = pd.to_datetime(tweets['Time'], format='%y-%m-%d %H:%M:%S')
# tweetsT = tweets['Time']
#
# trace = go.Histogram(
#     x=tweetsT,
#     marker=dict(
#         color='blue'
#     ),
#     opacity=0.75
# )
#
# layout = go.Layout(
#     title='Tweet Activity Over Years',
#     height=450,
#     width=1200,
#     xaxis=dict(
#         title='Month and year'
#     ),
#     yaxis=dict(
#         title='Tweet Quantity'
#     ),
#     bargap=0.2,
# )
#
# data = [trace]
#
# fig = go.Figure(data=data, layout=layout)
# py.offline.iplot(fig)
