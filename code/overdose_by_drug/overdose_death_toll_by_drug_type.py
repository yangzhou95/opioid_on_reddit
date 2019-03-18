#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


import os


# In[5]:


os.getcwd()


# In[ ]:


filename ="./overdose.csv"


# In[29]:


os.chdir('/Users/zhou/Desktop/')


# In[62]:


df = pd.read_csv('overdose.csv', header=0)


# In[63]:


df.set_index('Year', inplace=True)
df


# In[55]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[110]:


ax=df.plot(figsize=[10,8],y=["Total_Overdose_Deaths","Any_Opioid","Prescription_Opioids",
                    "Cocaine","Heroin","Fentanyl","Methamphetamine","Benzodiazepines","Antidepressants"
                   ],colormap='Paired',style=['r-o',
                    'b--.',
                    'y-2',
                    'g-*',
                    'c-x',
                    'b-<',
                    'm->',
                    'k-d',
                    'm--1'
                   ])
plt.ylabel('Death',fontdict={'family':'arial','size':14})
plt.xlabel('Year',fontdict={'family':'arial','size':14})
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend(loc=0,prop={'size': 13})

plt.savefig("overdose_death.eps")


# In[66]:





# In[77]:


ax = df.plot(style=['r-o',
                    'b--.',
                    'y-,',
                    'g-*',
                    'c-x',
                    'b-<',
                    'm->',
                    'k-d',
                    'm--1'
                   ])


# In[79]:


font = {'family' : 'arial',
        'weight' : 'normal',
        'size'   : 22}


# In[ ]:




