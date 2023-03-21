dogs = {
    'Name':['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max', 'Stella', 'Bernie'],
    'Breed':['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard'],
    'Color':['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White'],
    'Height':[56,43,46,49,59,18,77],
    'Weight':[25,23,22,18,29,2,75],
    'Date of Birth':[2013,2016,2014,2011,2017,2015,2018]
}
from numpy.lib.function_base import average
import pandas as pd
import matplotlib.pyplot as plt
dog = pd.DataFrame(dogs)

#刪除重複值
# dog = dog.drop_duplicates('Breed') #刪除重複的資料
# dog = dog.drop_duplicates(subset = ['Breed', 'Name'])

#記數
# print(dog['Breed'].value_counts()) #記數
# print(dog['Breed'].value_counts(sort = True)) #按數值多到少排序
# print(dog['Breed'].value_counts(normalize = True)) #按照量的多寡以比例來表示

# Grouped
# print(dog[dog['Color'] == 'Brown']['Weight'].mean()) #這個做法要一個一個打，很麻煩
# print(dog.groupby('Color')['Weight'].mean()) #這樣會show全部的Color
# print(dog.groupby('Color')['Weight'].agg([min, max, average]))
# print(dog.groupby(['Breed', 'Color'])['Weight'].mean())
# print(dog.groupby(['Breed', 'Color'])['Weight', 'Height'].mean())
# print(dog.pivot_table(values = 'Weight', index = 'Color')) #樞紐分析,是一種匯總資料的方式
import numpy as np
# print(dog.pivot_table(values = 'Weight', index = 'Color', aggfunc = np.median))
# print(dog.pivot_table(values = 'Weight', index = 'Color', aggfunc = [np.median, np.mean]))
print(dog.groupby(['Color', 'Breed'])['Weight'].mean())
print(dog.pivot_table(values = 'Weight', index = 'Color', columns = 'Breed', fill_value = 0, margins = True)) #column 是會把各種Breed放在變項列，fill_value 是用0代替遺漏值，margins 是幫你計算各欄列的平均數