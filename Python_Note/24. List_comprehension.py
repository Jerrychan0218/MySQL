from re import I
import pandas as pd
# 當我們想把一個list裡的東西全部各自+1，我們有兩種做法
# 1.
# nums = [12, 8, 21, 3, 16]
# new_nums = []
# for num in nums: # 1. for loop
#     new_nums.append(num + 1)
#     print(num_nums)

# 2.
# nums = [12, 8, 21, 3, 16]
# new_nums = [num + 1 for num in nums]
# print(new_nums)

# 應用
# result = [num for num in range(11)]
# print(result)

# 巢套(Nested)loop，同樣有兩種做法
# 1.
# pairs_1 = []
# for num1 in range(0,2):
#     for num2 in range(6, 8):
#         pair_1.append((num1, num2)
# print(pairs_1) #出來的結果是[(0, 6), (0, 7), (1, 6), (1, 7)]，因為先處理local再處理global所以x 會是0011，而不是0101

# 2.
# pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
# print(pairs_2)

# 創造一個五行 0,1,2,3,4 的矩陣
matrix = [[col for col in range(5)] for row in range(5)] #col for col in range(5)會生成一col包含0,1,2,3,4，接著for row in range(5)則會生成五個row的0,1,2,3,4
# Print the matrix
for col in matrix:
    print(col)
# for row in matrix:
#     print(row)

# 直接寫條件式for loop
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# 另一種寫法
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
print(new_fellowship)

#dictionary 的寫法
a = {num: -num for num in range(9)} #這邊要用{} 而不是[]
print(a)
#例子2
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = {member: len(member) for member in fellowship}
print(new_fellowship)

#generator 假設要生成0到n的序列
def num_sequence(n):
    i = 0
    while i < n: #當滿足這條件，就會進入到while迴圈裡
        yield i #他無須像iter那樣要一直next()，他會自動生成自動跑
        i += 1
 
# homework
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
def get_lengths(input_list):
    for person in input_list:
        yield len(person)
for value in get_lengths(lannister):
    print(value)

# output expression for iterator variable in iterable 是最基本的comprehension展現的形式
 def lists2dict(list1, list2):
    zipped_lists = zip(list1, list2) #壓縮這兩個list
    rs_dict = dict(zipped_lists) # 把兩個list的結合體變為dictionary
    return rs_dict #回傳rs_dict對應lists2dict

rs_fxn = lists2dict(feature_names, row_vals)
print(rs_fxn)

# Open a connection to the file
with open('world_dev_ind.csv') as file:
    # Skip the column names
    file.readline()
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}
    # Process only the first 1000 rows
    for j in range(0,1000):
        # Split the current line into a list: line
        line = file.readline().split(',')
        # Get the value for the first column: first_col
        first_col = line[0]
        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1
# Print the resulting dictionary
print(counts_dict)

#example
# Initialize an empty dictionary: counts_dict
counts_dict = {}
# Open a connection to the file
with open('world_dev_ind.csv') as file:
    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
# Print            
print(counts_dict)
#產生dictionary，並用,分隔開

#chunk 分塊
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize = 10) #以10筆為一塊
# Print two chunks
print(next(df_reader))#第一塊
print(next(df_reader))#第二塊

#project example step1
# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000) #有超多筆資料，所以要用分塊來處理
df_urb_pop = next(urb_pop_reader) #先讀頭一個區塊
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB'] #我們要的只有'CountryCode' 是='CEB'的資料
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)']) #合併兩個column的資料
pops_list = list(pops) #把pops變成list

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list] #加一個col
#pops_list[0] = df_pop_ceb['Total Population']...pops_list[1] = df_pop_ceb['Urban population (% of total)']
#tup[0] 是指在pops_list裡的所有[0]
print(df_pop_ceb)

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population') #製圖
plt.show()

#project example step2 (創造一個dataframe)
import pandas as pd
import matplotlib.pyplot as plt
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()
# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader: #這邊df_urb_pop是還沒有定義的，是指在urb_pop_reader裡的所有東西

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb) #上面一直在創造df_pop_ceb的內容，所以這邊填滿了原本的空DataFrame(data)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

#project example step3 (define 成一個function可以輸入檔名同國家碼就可以生成圖)
# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')