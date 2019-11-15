#coding=utf-8
#字符串的拼接
a='heygor'
b=' is no.1'
print(a+b)
print(a+b[-1])
tel='0452-8869504'
print(tel[:5])
print(tel[5:])
print(tel[:5]+'6'+tel[5:])
#字符串的遍历
name='im your baba!'
for i in name:
    print(i)
#去空格
#strip()  去掉两边的空格
#lstrip() 去掉左边的空格
#rstrip() 去掉右边的空格
str1='    hello memeda!    '
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
#计算长度(元素个数)
#len() 计算元素个数
print(len(str1))
name=input('请输入用户名：')
if len(name)==0:
    print('请重新输入')
else:
    print('yes')