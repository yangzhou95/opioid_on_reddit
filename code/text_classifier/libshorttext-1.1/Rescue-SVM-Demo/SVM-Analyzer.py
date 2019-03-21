# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:40:27 2017

@author: jstuve
"""
import os
from sklearn.metrics import confusion_matrix

'''
Predict File is created through command line demo show in the READ.ME
'''
predict_file = os.getcwd() + '\\predict_results'

pred = []
act = []

with open(predict_file, 'r') as p_file:
    for line in p_file:
        line = line.split("\t")
        if(len(line) > 2):
            pred.append(line[0])
            act.append(line[1])

m = confusion_matrix(act, pred)

#Precision(p)  = (a)/(a+c) = (m[0,0])/(m[0,0]+m[1,0])
p = m[0,0] / (m[0,0] + m[1,0])

#Recall(r) = (a)/(a+b) = (m[0,0])/(m[0,0]+m[0,1])
r = m[0,0] / (m[0,0] + m[0,1])

#F-Measure(f) = (2*r*p)/(r+p)
f = (2*r*p) / (r + p)

print("Precision: " + str(p))
print("Recall: " + str(r))
print("F-measure: " + str(f))