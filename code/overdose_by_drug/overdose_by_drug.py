import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# print current working directory
print(os.getcwd())


filename = "overdose_death_toll_by_drug_type.csv"
df = pd.read_csv(filename)
print(df)