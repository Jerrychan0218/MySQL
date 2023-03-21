#要檢驗string是否有不同，會使用minimum edit distance的方法，也就是string之間的差異遠近
#而判定距離的方法有幾種，插入新字(insertion)，刪除字(deletion)，substitution(替代字)，transposition(換位)
#比如sing sign, 它們的差距就是1 'g','n'，方法是換位
from fuzzywuzzy import fuzz #fuzzywuzzy是最常用的字串比較工具

fuzz.WRatio('Reeding', 'Reading') #可以得出兩個字的相似度有多少，1-100，100就是一模一樣
#fuzz就算是用在
fuzz.WRatio('Reeding_Reading', 'Reading') #也是可以的，它沒有順序的問題

#另一種高端方法是
from fuzzywuzzy import process #有了這個，我們可以設定條件，來看看哪個最為相似，它會由高到低排序
string = 'reading books vs reeding shirt'
choice = pd.Series(['books vs shirt','shirt vs books','reading vs reeding', 'reeding vs reading'])
process.extract(string, choice, limit = 2) 
#它會return[('books vs shirt', 86, 0)]

#當資料很凌亂，有多個跟reading相似的字時，而我們又要把它們都變成reading
print(a['habit'].unique()) #先找出column裡不一樣的各種類別

#假設我們有一個dataframe是categories，裡面有一個column 'habit'，裡面只有reading跟playing，像是設定檔一樣，我們可以透過for loop來把所有錯字拼回reading
for habit in categories['habit']:
    matches = process.extract(habit, a['habit'], limit = survey.shape[0]) #limit這邊是調整長度為調查整個dataframe，利用a['habit']的內容對比habit有沒有對上，得出每個的相似度
    for potential_match in matches:
        if potential_match[1] >= 80: #potential_match[1]是指第2column的相似度，process.extract生成出來的。如果在matches裡的跟habit裡的有80%或更高相似度，則繼續執行
            a.loc[a['habit'] == potential_match[0], 'habit'] = habit #如果相似度大於等於80，
            #便找出在a['habit']裡的這些超過80的字串，並用potential_match[0]，也就是process.extract生成出來的東西的第一行，也就是categories['habit']裡的東西，來代替藍色habit，也就是a['habit']的內容

#example:
# Import process from fuzzywuzzy
from fuzzywuzzy import process
# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()
# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types))) #用unique_types 對比'asian'
# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))
# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))