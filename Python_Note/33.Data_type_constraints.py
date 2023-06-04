# Print the information of ride_sharing
print(ride_sharing.info()) #會顯示一些資料格式
# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe()) #顯示資料的描述統計

# Print the information of ride_sharing
print(ride_sharing.info())
# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')
# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category' #確認是不是已經轉換，如果是會回傳None
# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes') #刪掉這column中的'minutes'字串
# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int') #變成int格式
# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int' #確認是不是int格式
# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean()) #計算平均

#取代功能，如果有資料超過27就變成27
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int') #把column變int
# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27 #把大於27的改為27
# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category') #改回category
# Print tire size description
print(ride_sharing['tire_sizes'].describe()) #來個摘要描述統計

#取代功能，如果有資料超過今天日期就變成今天
# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date #把資料變為datetime格式
# Save today's date
today = dt.date.today()
# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today
# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

#也可以用drop來把不合心意的資料刪掉，以超過5為例子
ride_sharing.drop(ride_sharing[ride_sharing['tire_size']>5].index , inplace = True) #加入這行就變成刪掉了，inplace = True是指直接在原檔裡刪除，False會另外創新column為刪掉後的資料


#找尋重複值
# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', keep = False) #找尋ride_id有重複的，keep=False 代表保留全部，keep = first 代表保留較前面那一項，keep = last 保留較後面那一項
# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id') #從duplicates裡根據ride_id來排列
# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

#用其他方法處理重複資料
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates() #刪掉完全重複的
# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'} #當資料有重複，但birth_year有些許不一樣，我們取小的，duration則是用mean的方式來處理
# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index() #我們以ride_id作為分組依據，對每組使用statistic的功能，然後reset_index來使資料最後重新標註編號
# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False) #再檢查一次
duplicated_rides = ride_unique[duplicates == True]
# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0 #assert 斷言句


#處理類別變項有錯誤的情況
# Print categories DataFrame
print(categories) #airline 及category是不一樣的dataframe
# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n") #印出在airlines['cleanliness']裡所有不一樣的選項
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")


# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness']) #先找找這兩個Dataframe的cleanliness column裡有沒有不一樣的，然後就會顯示該項目是甚麼
# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean) #選取所有airlines的cleanliness column中有cat_clean所得出來的東西的整筆資料 
# Print rows with inconsistent category
print(airlines[cat_clean_rows]) #print出有異樣的row
# Print rows with consistent categories only
print(airlines[~cat_clean_rows]) # ~有drop的意義，所以這邊就捨棄了有異樣的row

##Series and DataFrame are pandas item
a = pd.Series([1, 2, 3, 4])
b = {'name':'apple','birth':'1995-02-18','luckynum':'7'}
c = pd.Series(b)
#輸出會是
#birth      1995-02-18
#luckynum   7
#name       apple
#dtype:object

#DataFrame 就是類似excel那樣
#.value_counts() 只能用在Series
#.count() 可以用在DataFrame，也可以用groupby().count()

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() #把東西變小寫
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'}) #取代eur為europe

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())
# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})
# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip() #括號中沒有東西等於空格，消除空格
# Verify changes have been effected
print(airlines['dest_size'].unique())
print(airlines['dest_region'].unique())

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']
# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, #cut可以擷取我們想呈現的範圍，這邊擷取了wait_min column，label_ranges 把資料分成三份，0-60, 60-180, 180-無限
                                labels = label_names) #labels 把0-60 設定為short，60-180為medium，180以上為long
# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}
airlines['day_week'] = airlines['day'].replace(mappings)

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","") #把Dr取代成空格
# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")
# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")
# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")
# ***airlines['full_name'] = airlines['full_name'].str.replace(r'\D+',"")****  r'\D+' 是指除了數字以外的所有東西，還有其他，可以參考DATA CAMP regular expression
# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False #str.contains('Ms.|Mr.|Miss|Dr.').any() == False，代表當有這些東西時，會回應False


# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()
# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]
# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40
# Print new survey_response column
print(airlines_survey['survey_response'])


# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year #這樣可以得出age
# Find rows where age column == ages_manual
age_equ = ages_manual == banking['age']
# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]
# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

