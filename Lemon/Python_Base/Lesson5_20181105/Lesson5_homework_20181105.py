# -*- coding: utf-8 -*-
# @Time     : 2018/11/5/20:47
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson5_homework_20181105.py
# @Software : PyCharm
'''
1. 寻找10到12岁的小女孩加入球队（包含10，12），询问用户的性别（男：m），（女：f）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
count = 0
for i in range(3):
    gender = input("请输入用户的性别(男:m,女:f)：")
    age = eval(input("请输入用户的年龄："))
    if gender in 'f':
        if 10 <= age <= 12:
            print("这个用户可以加入球队")
            count+=1
        else:
            print("这个用户不可以加入球队")
    else:
        print("这个用户不可以加入球队")
print("满足条件的总人数是{}人".format(count))

# 2. 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
a=[1,7,4,89,34,666,99,8,2,2]
for i in range(1, len(a)):
    for j in range(len(a)-i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

'''
3. 有一组用户的登录信息存储在字典 login_info 里面，
字典格式如下：login_info={"admin":"root","user_1":"123456"}
key表示用户名，value表示密码，请编写函数满足如下条件：
1)设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
2)首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入。
4)如果密码输入错误超过三次，中断程序运行。
5)当输入密码错误时，提示还有几次机会
6)用户名和密码都输入正确的时候，提示登陆成功!
'''
login_info={"admin":"root","user_1":"123456"}
username = input("请输入用户名：")
while username not in login_info.keys() or False:
    username = input("请输入正确的用户名：")

pwd = input("请输入密码：")
def fac(pwd):
    i = 3
    while i <= 3:
        if pwd in login_info[username]:
            print("登录成功")
            break
        elif i == 0:
            break
        print("密码错误，还有{}次机会".format(i))
        pwd = input("请重新输入密码：")
        i -= 1
if pwd in login_info[username]:
    print("登录成功")
else:
    fac(pwd)
