#當我們有兩個data，然後要合併起來，我們可以利用recordlinkage來做
#recordlinkage有別於merge function，他比較自由，不一定要兩個data都有同樣的column
from textwrap import indent
import recordlinkage
indexer = recordlinkage.Index() #我們先建立一個連結平台
indexer.block('state') #我們以state來作為兩個data要連接起來的column，並且兩個data的資料都會保留起來
pairs = indexer.index(a,b) # 告訴python我們的兩個data是a,b
print(pair)
#而當資料裡有些可能打錯而使合併有問題，我們就要...
compare_cl = recordlinkage.Compare() #創造一個比較平台
compare_cl.exact('date_of_birth', 'date_of_birth', label = 'date_of_birth') #我們希望a裡的'date_of_birth'與b的'date_of_birth'能完全合併在一起，並重新命名為'date_of_birth'
compare_cl.string('surname', 'surname', threshold = 0.85, label = 'surname') #threshold是指當他們有相似度0.85或以上才是我要的資料
potential_matches = compare_cl.compute(pairs, a, b) #這樣會產生出兩個data經過比較後哪些資料值有高於0.85，符合要求的，是1，不符合要求的為0
matches = potential_matches[potential_matches.sum(axis = 1) >= 3] #因為正在比的有三個變項，所以row加起來有3的，就代表是潛在可能是重複值的資料
print(matches)

matches.index #我們使用這個來找出matches的索引都有哪些，包含了a跟b，但因為a在前面b在後，形成了MultiIndex
#我們要把b獨立出來，就需要從multindex拿出來
duplicate_rows = matches.index.get_level_values(1) #get_level_values可以透過輸入column name或順序來把data整個抽出來
print(b_index)

b_duplicates = b[b.index.isin(duplicate_rows)] #看看b是否有重複值
b_new = b[~b.index.isin(duplicate_rows)] #看看b index有沒有跟a重複

#最後把兩個data結合起來
end = a.append(b_new)


#example
# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]
# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)
# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
