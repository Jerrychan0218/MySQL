# 第一題
for i in range(10):
    a = 0
    for j in range(1,10):
        a=a+i
        print(str(i)+'*'+str(j)+'='+str(a))

# 第二題
a=111
b=222
c=333
d=b
e=c

c=a
b=e
a=d

print(a,b,c)