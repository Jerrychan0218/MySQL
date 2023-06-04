from turtle import pd


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a = pd.read_csv('Coding.csv')
print(a.head())
sns.jointplot(x = 'MMAP', y = 'WPM', data = a, )
plt.show()

