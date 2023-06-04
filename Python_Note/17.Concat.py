import pandas as pd
pd.concat([a,b,c],ignore_index = True, keys=['a','b','c']) #將abc以打直方式合併成為一個長table, 要注意變項要一樣先可以
#ignore_index True左會幫你將本來合併之後都系各自排列既index改成從1到最尾既資料
#keys 會響表到加註邊d數據原本屬於邊個table
pd.concat([a,b,c], sort = Ture)
#sort true左會幫你將a表有而b表無既column都合併成一個表，而將b表無既部分na

#另一種做法append(比較似merge)
a.append([b,c], ignore_index = True, sort = True)

#要檢查合併後表內有沒有重複值可以用validate, validate係同python講我地想要既數據係one_to_one? one_to_many? many_to_one? many_to_many?
# 比如a表裡id變項，有兩個2號，合併之後就變成2會對到不同既野變成one_to_many既關係
a.merge(b,on='id',validate = 'one_to_one')
#就會有Error同你講因為有one_to_many響入面

#concat既validate係verify_integrity=True, 會幫手檢查有無重複值