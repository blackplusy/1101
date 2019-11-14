#coding=utf-8
#字符集
#utf-8  全球通用，翻译官
#GBK2312 中文字符集

#1.直接输出
#使用print函数输出内容
#输出字符串内容
print('heygor is handsome!!!')
#输出数字类型内容
print(250)

#2.变量输出
a=100
#a是变量的名字，100是变量的值
print(a)
a='heygor'
print(a)

a=30
b=20
print(a+b)

a='20'
b='30'
print(a+b)

#3.函数输出
#abs()   绝对值
#len()   计算元素的个数(长度)
print(abs(-10))
print(len('kouniqiwa'))

#4.格式化输出
'''
%s  格式化输出字符类型数据
%d  格式化输出数字类型数据
如果需要传入的数据只有一个可以不加括号
'''
name='小明'
no=1
print('%s is no.%d'%(name,no))

age=18
print('小明的年龄:%d'% age)


age='18'
print('小明的年龄:%d'% age)









