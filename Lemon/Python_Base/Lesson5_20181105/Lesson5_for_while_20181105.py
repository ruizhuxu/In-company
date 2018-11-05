# -*- coding: utf-8 -*-
# @Time     : 2018/11/5/20:39
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson5_for_while_20181105.py
# @Software : PyCharm

d = {1:2,'else':888,999:[11,"hester"]}
s = 'hester.xu'
for i in d:
    print(d[i])

a = 0
sum = 0
while a < 100:
    a+=1
    sum = sum + a
print(sum)

s = 0
for i in range(101):
    s += i
print(s)


