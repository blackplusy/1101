#coding=utf-8

#列表
l=['苍老师','武藤老师','加藤老师']
for i in l:
    print(i)
#元组
tup=(1,2,3,4)
for a in tup:
    if a%2==1:
        print('奇数')
    else:
        print('偶数')
#函数 range是范围函数
#range(10)    0-9
#range(1,10)  1-9
print('*'*10)
for i in range(10):
    print(i)

print('*'*10)
for i in range(1,10):
    print(i)

print('*'*10)
for i in range(-3,3):
    print(i)