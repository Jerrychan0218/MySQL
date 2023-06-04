dogs = {
    'Name':['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max', 'Stella', 'Bernie'],
    'Sex':['M',"F",'M','M',"F",'F','F'],
    'Breed':['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard'],
    'Color':['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White'],
    'Height':[56,43,46,49,59,18,77],
    'Weight':[25,23,22,18,29,2,30],
    'Date of Birth':[2013,2016,2014,2011,2017,2015,2018]
}
from numpy.lib.function_base import average
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dog = pd.DataFrame(dogs)

# dog['Height'].hist(bins = 10)
# plt.show()

# avg_dog_w = dog.groupby('Breed')['Weight'].mean()
# print(avg_dog_w)

# avg_dog_w.plot(kind = 'bar', title = 'Mean Weight by Dog Breed')
# plt.show()

# dog.plot(x = 'Date of Birth', y= 'Weight', kind = 'line', rot = 45) #rot是x軸的東西轉45度
# plt.show()

# dog.plot(x = 'Height', y = 'Weight', kind = 'scatter')
# plt.show()

# print(dog[dog['Sex'] == 'M']['Height'].hist())
# print(dog[dog['Sex'] == 'F']['Height'].hist())
# plt.show()

#處理Missing value
# print(dog)
# dog.isna() #告訴你是或不是missing value
# dog.isna().any() #尋找column裡有沒有missing value, 只會告知有或沒有
# dog.isna().sum() #統計不同column裡有多少missing value
# dog.isna().sum().plot(kind = 'bar') #用圖來顯示
# plt.show()
# dog.dropna() #刪除missing value
# dog.fillna(0) #用0代替missing value

# 讀csv
import pandas as pd
# new_dog = pd.read_csv('')
# dog.to_csv('new_dogs.csv') #存一個csv檔

#合併兩個DataFrame


