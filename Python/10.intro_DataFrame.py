dogs = {
    'Name':['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max', 'Stella', 'Bernie'],
    'Breed':['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard'],
    'Color':['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White'],
    'Height':[56,43,46,49,59,18,77],
    'Weight':[25,23,22,18,29,2,75],
    'Date of Birth':[2013,2016,2014,2011,2017,2015,2018]
}
import pandas as pd
dog = pd.DataFrame(dogs) 
# print(dog)
# print(dog.head()) #如同R, 只會顯示頭幾個dog的資料
# print(dog.info()) #顯示非常基本的架構資料，告知你資料種類
# print(dog.shape) #幾乘幾的架構
# print(dog.describe()) #描述統計，好用
# print(dog.values) #以array方式顯示架構
# print(dog.columns) #顯示變項名
# print(dog.index) #顯示有幾row

