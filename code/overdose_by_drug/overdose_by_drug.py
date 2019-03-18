import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# print current working directory
print(os.getcwd())
# setup your working directory to the place where the overdose data is saved
# os.chdir('~/Documents/github/opioid_on_reddit/code')


filename = "overdose.csv"
df = pd.read_csv(filename, header=0)
df.set_index('Year', inplace=True)

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

# setup the x tick labels
ax = plt.gca()
xticklabels = np.arange(1999, 2017, 1)
ax.set_xticklabels(xticklabels)
plt.show()
# save figure in *.eps format
plt.savefig("overdose_death.eps")