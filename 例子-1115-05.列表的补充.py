#coding=utf-8
l1=[1,2,3,4,5,6]
print(l1)
l1.append(7)
print(l1)
l1.append(8)
print(l1)
print('-----')
l1.pop()
print(l1)
l1.pop()
print(l1)
l1.pop()
print(l1)
#获取列表索引
l2=[1,2,3,4,5,2,3,4]
print(l2.index(4))
l3=[1,2,3,'1']
print(l3.index('1'))
for index,value in enumerate(l3):
    print('索引是'+str(index)+',值是'+str(value))

print('**********')
#列表的排序
l=[1,3,5,7,2,4,6,8]
l.reverse()
print(l)
l=[1,3,5,7,2,4,6,8]
l.sort()
print(l)

l=[1,3,5,7,2,4,6,8]
l.sort()
l.reverse()
print(l)

l=[1,3,5,7,2,4,6,8]
l.sort(reverse=True)
print(l)

#列表推导式
a=[1,2,3,4]
print([5 * x for x in a])
#没有给定列表时候可以使用range方法
print([3*x for x in range(10)])
#加入if条件进行推导
print([x for x in a if x%2==0])
#多个for语句进行推导
print([[x,y] for x in range(2) for y in range(2)])

