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

#篩選要法
# print(dog.sort_values('Weight')) #以Weight為基準排序整個資料
# print(dog.sort_values('Weight', ascending = False)) #以Weight為基準排序資料，但是從大排到小
# print(dog.sort_values(['Height','Weight'])) #這邊指定了兩個變項，所以要用[]，根據這兩個來排序
# print(dog.sort_values(['Height', 'Weight'], ascending=[True, False]))
# print(dog['Name'])
# print(dog[['Height', 'Weight']]) #挑出height, weight兩column
# print(dog['Height'] > 50) #問是否
# print(dog[dog['Height'] > 50]) #問數值
# print(dog[dog['Breed'] == 'Labrador']) 
# print(dog[dog['Date of Birth'] > 2015])
# Lab = dog['Breed'] == 'Labrador'
# is_brown = dog['Color'] == 'Brown'
# print(dog[Lab & is_brown])
# is_black_or_brown = dog['Color'].isin(['Black','Brown']) #isin會顯示括號裡的東西，等同於or function
# print(dog[is_black_or_brown])

# 增加column
dog['Height_m'] = dog['Height'] /100
dog['bmi'] = dog['Weight']/dog['Height_m'] ** 2  
dog_bmi_100 = dog[dog['bmi'] < 100]
dog_bmi_100_height = dog_bmi_100.sort_values('Height', ascending = False)
print(dog_bmi_100_height[['Name', 'Breed', 'bmi']])
