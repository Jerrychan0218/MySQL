pop = [30.55, 2.77, 39.21]
countries = ['HK', 'TW', 'MAL']
ind_alb = countries.index("MAL") #index 會回傳目標的位置
print(ind_alb)

print(pop[ind_alb]) #pop 裡 MAL 的相對位置的數值

world = {'HK':30.55, 'TW':2.77, 'MAL':39.21} #dictionary
print(world['TW']) #回傳對應的數值
print(world)
world['SE'] = 1.68
print(world)
print('SE' in world)
del(world['SE']) #del會連對應的數字都刪掉
print(world)