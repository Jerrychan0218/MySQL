# import numpy as np
# np_height = np.array([1.76, 1.69, 1.73, 1.43])
# np_weight = np.array([65.4, 59.2, 63.6, 88.4])
# bmi = np_weight / np_height ** 2
# print(bmi)
# print(bmi > 23) #這比較像是問array裡的直是否大於 bmi 23，出來會是「是或否」
# print(bmi[bmi > 23]) #這比較像是問bmi array裡bmi > 23的值是多少。 

# # Comparison Operators
# # >
# # <=
# # >
# # >=
# # == #等於
# # != #不等於

# #Boolean Operators (and, or, not)
# #用numpy來弄的話
# print(np.logical_and(bmi > 21, bmi < 22)) #得是否
# print(bmi[np.logical_and(bmi > 21, bmi < 22)]) #得值

# if elif else
z = int(input('請輸入數字'))
if z % 2 == 0: # z % 2 == 0, 代表z 除 2 後餘數 = 0
    print('checking '+ str(z))
    print('the number is even')
else:
    print('the number is odd')


