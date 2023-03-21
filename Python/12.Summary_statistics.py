dogs = {
    'Name':['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max', 'Stella', 'Bernie'],
    'Breed':['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard'],
    'Color':['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White'],
    'Height':[56,43,46,49,59,18,77],
    'Weight':[25,23,22,18,29,2,75],
    'Date of Birth':[2013,2016,2014,2011,2017,2015,2018]
}
import pandas as pd
import numpy as np
dog = pd.DataFrame(dogs)

# print(dog['Height'].mean())
# print(dog.describe())

# def pct30(column):
#     return column.quantile(0.3) #求出30%的數值
# def pct40(column):
#     return column.quantile(0.4)

# print(dog['Weight'].agg(pct30))
# print(dog[['Height', 'Weight']].agg(pct30))
# print(dog['Weight'].agg([pct30, pct40]))

# print(dog['Weight'].cumsum()) #累積加總
# print(dog['Weight'].cummax()) #一個一個順下來，列出目前遇到最大值是多少
print(dog['Weight'])
print(dog['Weight'].cumprod()) #累積乘積