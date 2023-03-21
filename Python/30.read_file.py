!ls #直接可以告訴你你現在正在開啟的檔案是甚麼

# Open a file: file
file = open('moby_dick.txt', mode = 'r') # r 代表read only，w代表write
# Print it
print(file.read())
# Check whether file is closed 
print(file.closed) #r檢查file是不是關掉了
# Close file
file.close() #把file關掉
# Check whether file is closed
print(file.closed)

# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
#flat file = txt/csv

#numpy可以把資料快速地變為array，主要使用loadtxt及genfromtxt來讀txt檔
import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter = ',', skiprows=1, usecols=[0,2], dtype = str)  
#delimiter分隔符號，skiprows=跳過第一行，usecols=要用第一跟第二col的資料，dtype使讀檔時全部資料都以str的方式呈現
data

# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv' #這是一張圖
# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')
# Print datatype of digits
print(type(digits))
# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28)) #這是在製定圖的大小
# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest') #cmap背景顏色，interpolation =使用最近的顏色來決定像素的群集
plt.show()

# Import numpy
import numpy as np
# Assign the filename: file
file = 'digits_header.txt'
# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2]) #\t是 tap-delimited是用分行來分隔資料的意思
# Print data
print(data)

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)
# Print the first element of data
print(data[0])
# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
# Print the 10th element of data_float
print(data_float[9])
print(data)
# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1]) #x是所有第0 col的所有row，則是第2col的所有值
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


#我們可以用np.genfromtxt來讀csv，也可以用np.recfromcsv
# Assign the filename: file
file = 'titanic.csv'
# Import file using np.recfromcsv: d
d = np.recfromcsv(file, delimiter = ',', names = True, dtype = None) #其實默認也是dtype = None
# Print out first three entries of d
print(d[:3])


#實際示範一次
# Assign the filename: file
file = 'digits.csv'
# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows = 5, header = None) #這樣只會顯示5行
# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)
# Print the datatype of data_array to the shell
print(type(data_array)) 

#續
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Assign filename: file
file = 'titanic_corrupt.txt'
# Import file: data
data = pd.read_csv(file, sep='\t', comment= '#', na_values='Nothing')
# Print the head of the DataFrame
print(data.head())
# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# Import pickle package
import pickle
# Open pickle file and load data: d
with open('data.pkl', 'rb') as file: #rb 是指read only, 並且是二元binary資料 
    d = pickle.load(file)
# Print d
print(d)
# Print datatype of d
print(type(d))

# Import pandas
import pandas as pd
# Assign spreadsheet filename: file
file = 'battledeath.xlsx'
# Load spreadsheet: xls
xls = pd.ExcelFile('battledeath.xlsx')
# Print sheet names
print(xls.sheet_names) #可以print出分頁的名稱

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004') #這個xls有兩個分頁，用parse可以單獨讀取'2004'/'2002'分頁，這樣比較好處理與分析
# Print the head of the DataFrame df1
print(df1.head())
# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0) #因為分頁第一個是'2002'
# Print the head of the DataFrame df2
print(df2.head())

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=1, names=['Country', 'AAM due to War (2002)'])
# Print the head of the DataFrame df1
print(df1.head())
# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=1, names= ['Country']
# Print the head of the DataFrame df2
print(df2.head())

#讀SAS檔 *statistic的簡稱
# Import sas7bdat package
from sas7bdat import SAS7BDAT
# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()
# Print head of DataFrame
print(df_sas.head())
# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()


#讀stata/dta檔 *statistic data的簡稱 
import pandas as pd
# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')
# Print the head of the DataFrame df
print(df.head())
# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

# Import packages
import numpy as np
import h5py 
# Assign filename: file #h5py是一種新興的資料檔，可以存非常大容量的資料
file = 'LIGO_data.hdf5'
# Load file: data
data = h5py.File(file, 'r')
# Print the datatype of the loaded file
print(type(data))
# Print the keys of the file
for key in file:
    print(key)

# Get the HDF5 group: group
group = data['strain']
# Check out keys of group
for key in group.keys():
    print(key)
# Set variable equal to time series data: strain
strain = np.array(data['strain']['Strain'])
# Set number of time points to sample: num_samples
num_samples = 10000
# Set time vector
time = np.arange(0, 1, 1/num_samples) #np.arange = range, (0,1,1) = range(0,1)，以1作為分隔，這邊最後一個1/10000，所以會以0.00001作為分隔
# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

#讀mat檔
# Import package
import scipy.io
# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
# Print the datatype type of mat
print(type(mat))


# Print the keys of the MATLAB dictionary #看看key是哪些變項，value就是變項的值
print(mat.keys())
# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))
# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt'])) #看看是幾乘幾的矩陣
# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()