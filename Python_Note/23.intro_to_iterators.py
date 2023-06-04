from re import A


word = 'Da'
it = iter(word)
next(it)#會先跑出'D'
next(it)#會跑出'a'

#也可以
word = 'data'
it = iter(word)
print(*it)

#也可以用在dictionary
a = {'hugo':'a', "chen":'b'}
for key, value in a.items():
    print(key, value)

#也可以用在讀檔案的每一行
file = open('a.txt')
it = iter(file)
print(next(it)) #印出第一行
print(next(it)) #印出第二行

#enumerate 可以幫list裡的東西排序，列出序列
a = ['baba','babr','adr']
for index, value in enumerate(avergers):
    print(index, value)

#zip 可以將兩個list的東西合併印出
a = ['adf','adsfs','aadf']
b = ['bfbab','dfbf','bddfb']
z = zip(a, b)
z = list(z)
print(z) #跑出全部

#or
for z1, z2 in zip(a,b):
    print(z1,z2) #跑出全部

#or
z = zip(a,b)
print(*z) #跑出全部

# unzip
result1, result2 = zip(*z1) #把z1裡的list按照順序解壓縮成兩個變項

#以for loop來處理大數據的東西，有時候數據量太多的時候
import pandas as pd
result = []
for chunk in pd.read_csv('data.csv', chunksize = 1000): 
# 因為數據量太大，chunksize則可以告訴電腦一次處理多少數據
    result.append(sum(chunk['x'])) #append加一行，那一行是x的加總
total = sum(result)
print(total)
total = 0 
for chunk in pd.read_csv('data.csv', chunksize = 1000):
    total += sum(chunk['x']) #total是累積x
print(total)

## Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize = c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)

