import pandas as pd
brics = pd.read_csv('test.csv')
brics.index = ['HKG','TP','JLP','BJ']


print(brics['area'])
print(brics['area'] > 8)
print(brics[brics['area'] > 8])

import numpy as np
s = np.logical_and(brics['area'] > 8, brics['area'] < 10) # 出來是是否
print(brics[s])
