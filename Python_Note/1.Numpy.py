import numpy as np
# height = [1.76, 1.69]
# weight = [57.4, 59]
# generally list can't calculate without Numpy
# BMI = weight / height ** 2 #Error

# np_height = np.array(height)
# print(np_height)
# np_weight = np.array(weight)
# print(np_weight)
# bmi = np_weight / np_height ** 2
# print(bmi)
# Numpy array 相加會真的加，普通的list 相加會是list合併
# np_2d = np.array([[1.76,1.69,1.48], #這樣就會生成表第一行會是1.76...
#                   [57.4,59,46.6]])
# print(np_2d)
# print(np_2d.shape) #有幾rows行幾列columns
# print(np_2d[0]) #叫第一行出來
# print(np_2d[0][2]) #叫第一行裡的第三個出來
# print(np_2d[0,2]) #同上
# print(np_2d[:,1:2]) #叫兩行的第二三個出來
# print(np_2d[1,:]) #叫第二行的全部出來

#numpy還可以用來弄統計
# print(np.mean(np_2d[:,0])) #第一列加起來算平均，直的平均
# print(np.median(np_2d[:,0])) #同上但是是算中位數
# print(np.corrcoef(np_2d[:,0], np_2d[:,1])) #第一列跟第二列的相關
# print(np.std(np_2d[:,0])) #第一列標準差

#numpy 生成亂數
height = np.round(np.random.normal(1.75, 0.2 , 5000), 2) #生成數據，round是多少小數點，np.random.normal(平均,標準差,數量)
weight = np.round(np.random.normal(60.4, 15 , 5000), 2)
np_city = np.column_stack((height, weight)) #產出兩列，height是第一列，weight是第二
print(np_city)