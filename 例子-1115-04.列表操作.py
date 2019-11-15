#coding=utf-8
l=['kobe','rose','AI']
#列表的访问
#1.直接访问
print(l)
#2.遍历访问
for i in l:
    print(i)
#3.成员访问
if 'kobe' in l:
    print('24')
#索引和切片
l=[1,3,5,7,9]
print(l[0])
print(l[-3])
print(l[:-2])
print(l[1:3])
print(l[::-1])
#列表的修改
l=[1,3,5,7,9]
print(l)
l[2]=0
print(l)
l[-3]=999
print(l)
#列表的拼接
l=[1,2,3]
l1=['a','b','c']
print(l+l1)
print(str(l[0])+l1[2])

#列表的删除
l=[1,2,3,4,5]
print(l)
del l[1]
print(l)
del l
print(l)
