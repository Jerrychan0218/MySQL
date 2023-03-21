#While loop 是重複if，直到情境用完
#現在來個情境，開始是50，不斷除4，直到餘值不大於1
# error = 50
# while error > 1:
#     error = error / 4
#     print(error)

#for loop
#要逐一print出list裡的數值會很麻煩，用for loop會簡單多
# fam = [1.73, 1.68, 1.71, 1.89]
# for a in fam:
#     print(a)
# for index, height in enumerate(fam): #用了enumerate, 就會多了[(1, 1.73), (2, 1.68)...]也就是index 
#     print('index' + str(index) + ': ' + str(height))

#for loop 也可以用在string上
# for a in 'family':
#     print(a.capitalize())

# for loop 也可以用在dictionary
# world = {'HK':100,
#          'TW':200,
#          'MAL':300}
# for a, b in world.items(): #加items()才可以在dictionary中取出列表的所有key(a):values(b)
#     print(a + '--' + str(b))

#for loop 用在numpy
# import numpy as np
# np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# np_weight = np.array([60.3, 70.1, 55.3, 77.7, 80.9])
# meas = np.array([np_height, np_weight])
# bmi = np_weight/np_height ** 2
# for a in bmi: # 列出bmi中的值
#     print(a)
# for b in meas: # 列出兩個array
#     print(b)
# for c in np.nditer(meas): #逐一列出meas中的數值
#     print(c) 

# for loop 用在已有文件
import pandas as pd
brics = pd.read_csv('test.csv')
brics.index = ['HKG','TP','JLP','BJ']
# for a in brics:
#     print(a) #輸出變項名
# for index, row in brics.iterrows(): #iterrows是遍列的意思，先輸出每個index，然後把index中的資料逐一列出
#     # print(index)
#     # print(row)
#     # print(index + ': ' + row['capital'])
#     brics.loc[index, 'length'] = len(row['country']) #加一column
# print(brics)
brics['length'] = brics['country'].apply(len) #也是加一行，但這邊是用apply來執行len的function
print(brics)


