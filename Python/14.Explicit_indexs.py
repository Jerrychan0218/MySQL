dogs = {
    'Name':['Bella', 'Charlie', 'Lucy', 'Cooper', 'Max', 'Stella', 'Bernie'],
    'Breed':['Labrador', 'Poodle', 'Chow Chow', 'Schnauzer', 'Labrador', 'Chihuahua', 'St. Bernard'],
    'Color':['Brown', 'Black', 'Brown', 'Gray', 'Black', 'Tan', 'White'],
    'Height':[56,43,46,49,59,18,77],
    'Weight':[25,23,22,18,29,2,75],
    'Date of Birth':[2013,2016,2014,2011,2017,2015,2018]
}
from numpy.lib.function_base import average
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dog = pd.DataFrame(dogs)

# dog_ind = dog.set_index("Name")
# print(dog.index)
# print(dog_ind)
# print(dog_ind.reset_index()) #取消index
# print(dog_ind.reset_index(drop = True)) #取消之餘，把Name的Column都刪掉
# print(dog[dog['Name'].isin(['Bella', 'Stella'])]) #isin = or
dog_ind2 = dog.set_index(['Breed', 'Color']).sort_index()
print(dog_ind2)
# print(dog_ind2.sort_index(level = ['Color'], ascending = True)) #跟sort_values一樣，可以排序也可以調整順序

