import pandas as pd
a = pd.read_csv('co.csv', parse_dates = ['Start date', 'end date'])
#parse_dates會使python讀取資料中這兩個column並把它們視為日期資料
#可以一個中括號裡輸入兩個，不用[], []
#又或是可以
a['start date'] = pd.to_datetime(a['start date'], format = '%Y-%m-%d %H:%M:%S')
print(a.head(3))

a['duration'] = a['end'] - a['start']
a['duration'].dt.total_seconds().head(5) #記得要加dt

#average duration by month
a.resample('M', on = 'Start date')['Duaration seconds'].mean()
#代表針對Start date這個column，利用月份作為分組，計算每個月Start date的Duration seconds平均是多少
#這是除了groupby以外，另外一種分組方式

a.resample('M', on = 'Start date')['Duaration seconds'].plot() #可以直接畫圖

a['Start date'].head(3).dt.tz_localize('America/New_York')
#dt.tz_localize('America/New_York') 後會告訴你跟UTC的差異

#但因為有些資料有夏令時間的差別，導致整筆資料設定'America/New_York'的話，會有錯誤
a['Start date'].head(3).dt.tz_localize('America/New_York', ambiguous = 'NaT') #這樣就會把一些無法辨識的資料標註成Not a time，忽略掉

a['End date'].shift(1).head(3) #shift代表在原資料中加入幾行row

#如果想換到別的國家，則可以使用dt.tz_convert('別洲/別城市')



#example
# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                						 ambiguous='NaT')
# Print first value
print(rides['Start date'].iloc[0])
# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')
# Print the new value
print(rides['Start date'].iloc[0])

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.day_name()
# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))
# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()
# Resample to the month
monthly = rides.resample('M', on = 'Start date')
# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))