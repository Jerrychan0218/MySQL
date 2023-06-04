# 簡單製作DataFrame
dict = {
    'country':['HK','TW','MAL','CHI'],
    'capital':['A', 'B', 'C', "D"],
    'area':[8.516, 17.10, 3.286, 9.597],
    'population':[200,100,150,400]
}

import pandas as pd
# brics = pd.DataFrame(dict) #pd.DataFrame()來製作出dataframe
# print(brics)
# brics.index = ['HK','TW','MAL','CHI']
# print(brics)

#or 如果有現成的CSV檔，就可以先放在python文件夾，然後...
brics = pd.read_csv('test.csv')
# brics = pd.read_csv('test.csv', index_col = 0) #index_col = 0 代表把第一列往前挪
brics.index = ['HKG', 'TP', 'JLP', 'BJ']
#print(brics)

#選取Column
print(brics['country'])
print(brics[['country']]) #這樣會連變項名country也印出來
print(brics[['country', 'capital']]) #要取出兩列column，就要連標題一起才有辦法
# print(type(brics['country']))
print(brics[1:4]) #取出Row 第二行到第四行的資料

#取出特定資料（loc, iloc) loc是文字，iloc是數值
print(brics.loc['HKG']) #會以直(1D)的方式呈現HKG這個row的資料
print(brics.loc[['HKG']]) #會以橫式(2D)呈現HKG這個row的資料
print(brics.loc[['HKG', 'TP', 'JLP']]) #會以橫式呈現HKG TP JLP 三個row的資料
print(brics.loc[['HKG','TP','JLP'],['country','capital']]) #橫式呈現三個row, 兩個column
print(brics.loc[:,['country','capital']]) #橫式所有row + 2 column
print(brics.iloc[[1]]) #橫式TP資料
print(brics.iloc[[1,2,3]]) #橫式HKG TP JLP 三個row的資料
print(brics.iloc[[1,2,3], [0,1]]) #橫式3 row + 2 coloumn
print(brics.iloc[:, [0,1]]) #橫全 + 2 column

