#uniformity更換單位
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
#把它變成美金，所以乘以1.1
# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar' #assert 可以在code出現錯誤就直接Error，而不會出現數據跑完全部或崩潰才停

# Print the header of account_opened
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 
#infer_datetime_format = True 可以讓python讀取時間變項，把它調整成yyyy-mm-dd
#errors = 'coerce' 可以把無法轉型的資料變為NaN
# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')
# dt.strftime 擷取時間，'%Y'
# Print acct_year
print(banking['acct_year'])