import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
final_tail = []
for x in range(1000): #重複一千次
    tail = [0]
    for x in range(10): #拋10次硬幣，所以這邊是指10次中有最多10次是反面，重複一千次
        coin = np.random.randint(0,2) #正面或反面
        tail.append(tail[x] + coin) #不加coin永遠是0, 有反面就會加1
    final_tail.append(tail[-1]) #tail list 裡的最後一項
print(final_tail)
plt.hist(final_tail, bins = 10)
plt.show()

