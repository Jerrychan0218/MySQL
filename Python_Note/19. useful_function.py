import pandas as pd
a.query()
#用來篩選想要的資料，非常好用

a.melt(id_vars=[], value_vars=[],var_name= 'year', var_name='dollars')
#從橫的資料架構改為直的,id_vars[填入不用變為直式的變項，系統會把其他變項根據這裡不變的變項，作架構上的調整]
#value_vars是跟電腦說在要變的變項中哪些值是要顯示出來的
#var_name就是把轉換後的變項名稱variance改為想要的名字


pulls['date'] = pd.to_datetime(pulls['date'], utc = True)
#若資料裡有date的資料，可以先用上述code來使他格式變為datatime
#把原本2013-12-31T23:10:55Z 的時間資料變成2013-12-31 23:10:55+00
#utc是24小時制的意思
#然後
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
#可以把月，年分成兩行column

a.nlargest(10, 'user')
#可以將a裡的資料以user進行排序，並列出最高的十項
#通常會先
b = a.groupby('num').count()
#把資料計數之後再按照num來進行分組排列，只計算裡面有多少數字，不計0值
#我們可以用 num.size() 來確認有哪些組，以及每組有多少筆資料
#我們也可以用 b.get_group('c') 來展示num裡的c所包含的資料有哪些

set(a)
#會將a裡的變項或資料不重複的列出來

a['Weight'].unique() #可以不重複印出weight裡所有東西，

.append() 在表末加上新一行


a = parse('Hi, my name is {}, i am working in {}', 'Hi, my name is Jerry, i am working in HongKong')
#parse會幫我把Jerry 跟Hong Kong拿出來

a.unstack() #把table從直換成橫

#lambda算是簡單def
train_data['Name_cat'] = train_data.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip()) #把,前的東西分隔後刪掉
print(train_data['Name_cat'].value_counts())