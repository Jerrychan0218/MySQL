#合併兩個DataFrame
import pandas as pd
a = {
    'Name':['Chen','Wong','Chiu'],
    'age':[18,19,20],
    'level':[2,3,4]
}

b = {
    'Name':['Chen','Wong','Chiu'],
    'Dead_age':[36,77,80],
    'level':[99,80,55]
}
a = pd.DataFrame(a)
b = pd.DataFrame(b)
ab = a.merge(b, on = 'Name', how = 'outer', suffixes = ('_Newhand', '_Professional')) #要有column的資料是一樣的才能合併, suffixes是幫兩個DataFrame中名字一樣的變項名稱+東西，使得比較好辨認
print(ab)
# inner 系兩個table共有既數據default系呢個，left係左邊table同共有區域既，right同理，outer就係全部資料都呈現出黎