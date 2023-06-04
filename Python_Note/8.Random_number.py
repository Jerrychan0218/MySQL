# import numpy as np
# np.random.seed(2) #紀錄隨機數
# coin = np.random.randint(0,2) #這樣就只會生成0或1
# print(coin)
# if coin == 0:
#     print('head')
# else:
#     print('tails')
# print(np.random.rand()) #生成一個隨機數

#高級random function用法
# import numpy as np
# np.random.seed(1) 
# outcomes = [] #創一個空集合
# for x in range(10): #跑10次  
#     coin = np.random.randint(0, 2)
#     if coin == 0:
#         outcomes.append('heads') #append 會幫你在結果後面加入新結果
#     else:
#         outcomes.append('tail')
# print(outcomes)

import numpy as np
np.random.seed(3)
tail = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tail.append(tail[x] + coin)
print(tail)