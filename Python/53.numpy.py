import numpy as np

#array##########################
list1 = [1,2,3,4,5,6,7,8,9]
array1 = np.array(list1)
array1

#zeros########################
numpy.zeros((5,3))
#會生成一個5row,3column的矩陣

#np.random.random#######################
np.random.random((2,4)) #np.random是一系列模組，其中的random function，所以是np.random.random
#會生成一個2x4隨機亂數矩陣，數值會由0-1之間

#np.arange()#######################
np.arange(-3, 4)
#生成從-3至3的array，頭數計，尾數不計，默認是整數
np.arange(4)
#生成從0-3的list
np.arange(-3,4,3)
#生成-3至3的list，但間隔是3

from matplotlib.pyplot import pyplot as plt
plt.scatter(np.arange(0,7), np.arange(-3,4)) #x = 0-6；y = -3-3
plt.show()

#shape####################
np.shape(a) #顯示維度，(5,3) = 5row, 3column

#flatten()##################
array = np.array([1,2], [5,7], [6,6])
array.flatten()
#會合併本來有三維的array，變到一維\

#reshape####################
array = np.array([1,2], [5,7], [6,6])
array.reshape((2,3))
#會變為 [[1,2,5],
#        [7,6,6]]

#numpy dtype################
zero_array = np.zeros((3,2))
print(zero_array.dtype) #用來了解array裡的東西是甚麼Type
#====================================

# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3, 2))
# Print the data type of zero_array
print(zero_array.dtype)
# Create a new array of int32 zeros with three rows and two columns
zero_int_array = np.zeros((3,2), dtype = np.int32)
# Print the data type of zero_int_array
print(zero_int_array.dtype)

#換type = astype
# Print the data type of sudoku_game
print(sudoku_game.dtype)
# Change the data type of sudoku_game to int8
small_sudoku_game = sudoku_game.astype(np.int8)
# Print the data type of small_sudoku_game
print(small_sudoku_game.dtype)

#numpy location 選取範圍##########################
tree_census[0, 1] #第一row，第一column，tree_census是array
every_other_diameter = tree_census[50:101:2, 2] #row從50到100，每隔2來選取，column是2
print(every_other_diameter)

sorted_trunk_diameters = np.sort(tree_census[:,2], axis = 0) #sort是排序，axis是讓資料打直的排序還是橫的，1就是橫的，左是最小值，右是最大值。0是直的，上是最小，下是最大
print(sorted_trunk_diameters)

#filtering arrays 篩選資料#################### 
np.where(data, '資料中要被篩選的東西', '要取代的東西', '其他沒被篩選的東西的取代的東西')
np.where(data, '0', '', data) #data裡的0要變成空格，其他沒被取代的就按照data原本的樣子就好。


# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:,2] == 51]
print(largest_tree_data)

# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:,1] == 313879)
print(row_indices) #會生成符合313879的位置
# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879) #會生成位置的資料室哪些，這樣切換來切換去

#adding and removing data##############
np.concatenate((a ,b)) #python自動協助看兩個資料的矩陣是否合乎合併條件，以row形式優先，*********記得要雙括弧
np.concatenate((a, b), axis = 1) # b會以column方式從右邊插入a，達成合併 
np.concatenate((a,b), axis = 0) # b會以row方式從下邊插入a，達成合併 
#a b 需要有一樣的row或column數，row數一樣，可以執行column方式合併，column一致則可以row形式合併
# 1D 例如:shape(3,) 的array沒辦法使用合併功能，至少要2D (3,1)，所 以要合併3row 1column的矩陣，要先轉換成2D，或確認好是2D

array_1D = np.array([1,2,3]) 
array_1D.reshape((3,1)) #兩個長得一樣，但一個是1D，reshape後的是2D

# np.concatenate無法憑空增加維度

#Delete################################
np.delete(data, 要delete的行列位置, axis = 0) #axis代表是row
np.delete(data, 1, axis = 0) #delete 第2row的資料


#total#################################
# Create a 2D array of total monthly sales across industries
monthly_industry_sales = monthly_sales.sum(axis = 1, keepdims = True) 
#axis = 1 橫的sum，keepdims = True 會把生成出來的資料存成一個2D array
print(monthly_industry_sales)

#vectorized operation##################
#不論是加減乘除都可以直接很直覺的去做，會對整個array有效果，
# Create an array of tax collected by industry and month
tax_collected = monthly_sales * 0.05
print(tax_collected)
# Create an array of sales revenue plus tax collected by industry and month
total_tax_and_revenue = monthly_sales + tax_collected
print(total_tax_and_revenue)

# Create an array of monthly projected sales for all industries
projected_monthly_sales = monthly_sales * monthly_industry_multipliers
print(projected_monthly_sales)

# Graph current liquor store sales and projected liquor store sales by month
plt.plot(np.arange(1,13), monthly_sales[:,0], label="Current liquor store sales")
plt.plot(np.arange(1,13), projected_monthly_sales[:,0], label="Projected liquor store sales")
plt.legend()
plt.show()

#有些function本身是python內建的而不是numpy的，會令function只會對array的第一個數值有效，但我們可以透過np.vectorize()來讓function變成numpy可用的形式
# Vectorize the .upper() string method
vectorized_upper = np.vectorize(str.upper)

# Apply vectorized_upper to the names array
uppercase_names = vectorized_upper(names) #names的type是array
print(uppercase_names)


#broadcasted################################
#有點類似上面對array加減乘除，但會更快，
#需要從右到左去看兩個資料的維度，如果兩個資料的維度符合標準，我們就可以用broadcasted方法。row column維度只要符合其中一種要求就可以了。
#1. a = shape(10,5), b = shape(10,1)；從左到右看維度，5 & 1，符合第一種要求，即兩個資料要有一個是1
#2. 10, 10 符合第二個要求，兩個矩陣維度一樣ㄌㄨㄚ


# saving loading arrays
# numpy 可以讀csv txt pkl
# 還有npy，這是屬於numpy的專屬檔案，讀取速度會最快
# 要開npy 要用with open

rgb = np.array([[[255, 0, 0], [255, 0, 0], [255, 0, 0]],
                [[0, 255, 0], [0, 255, 0], [0, 255, 0]],
                [[0, 0, 255], [0, 0, 255], [0, 0, 255]]]) #這是色格的array，每一個1D array 分別代表紅綠藍，這邊有九格，分別代表不同顏色

with open('logo.npy', 'rb') as f: #rb 2進制執行r，r是唯讀
    logo_rgb_array = np.load(f)
plt.imshow(logo_rgb_array) #im = image，讀取img
plt.show()

dark_logo_array = np.where(logo_rgb_array == 255, 50, logo_rgb_array) #用where function的取代功能把array裡的255改成50，使顏色變暗
plt.imshow(dark_logo_array)
plt.show()

#要儲存dark version 可以用近似讀取的code
with open('dark_logo.npy', 'wb') as f: #wb 是指二進制執行w，w代表可以寫入的檔案，還有r, rb, w, wb, a, ab，r+, rb+, w+, wb+, a+, ab+ 代表兼加唯獨與寫入、添加與唯獨
    np.save(f, dark_logo_array)

#我們也可以用help(np.shape)、help(np.ndarray.flatten) #當method是array的function就要加ndarray


#array acrobatics array 雜技####################
np.flip() #可以反轉數組，換言之可以旋轉圖
#flip 會上下，左右，顏色全部翻轉，我們可以透過設定np.flip的內容來決定有哪些東西不改。
filpped_rows_logo = np.flip(logo_rgb_array, axis = 0) #axis = 2 = 改顏色，axis = (0, 1) = 上下左右轉
plt.imshow(flipped_rows_logo)
plt.show()

transpose_logo = np.transpose(logo_rgb_array, axes = (1,0,2)) #axe是把三個column順序改變，變成第二column在第一column，第一col改到第2 col....
plt.imshow(transposed_logo)
plt.show()

array = np.array([[1.1, 1.2, 1.3],
                  [2.1, 2.2, 2.3],
                  [3.1, 3.2, 3.3],
                  [4.1, 4.2, 4.3]]) #****第一column是控是上下，第二控制左右，第三顏色****

np.flip(array)

#array([[4.3, 4.2, 4.1],
#       [3.3, 3.2, 3.1],
#       [2.3, 2.2, 2.1],
#       [1.3, 1.2, 1.1]])

np.transpose(array)
#array([[1.1, 2.1, 3.1, 4.1],
#       [1.2, 2.2, 3.2, 4.2],
#       [1.3, 2.3, 3.3, 4.3]]) 

#split 分拆 ###################
red_array, green_array, blue_array = np.split(rgb, 3, axis = 2) #要拆的數組、拆分後row column的量、要拆分的軸
red_array

#stack 結合########################
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)

# Print q1_sales
print(q1_sales)

# Stack the four quarterly sales arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales], axis = 0)
print(quarterly_sales)