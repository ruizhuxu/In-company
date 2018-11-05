# -*- coding: utf-8 -*-
# @Time     : 2018/11/4/17:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson4_dictionary_20181102.py
# @Software : PyCharm

# input: 从控制台获取一个数据，但是这个数据都是字符串类型
# data = input("请输入一个数据：")
# print(data)
# print("类型:",type(data))

# 1 字典 --
# 2 空字典：d={}
# 3 key:value  键值对
# 4 key不可变；value可以是任意类型
# 5 key支持整数/浮点数/字符串/元组（不可变）；不支持列表/字典（可变）
# 6 key 一般（90%）是字符串
# 7  无序
# 8 可变，支持增删改查
# 9 查询：字典名[key]   嵌套取值
# 10 查询出所有的keys：  字典名.keys()
# 11 查询出所有的values：字典名.values()
# 12 查询出所有的键值对：字典名.items()
# 13 指定删除： 字典名.pop(key)
# 14 随机删除：字典名.popitem()
# 15 修改和新增：key存在就是修改；key不存在就是新增
# 16


d = {12.0: 99, "class_id": "python12", "num": "104", "grade": [99, 88, 45, 66],
     "course": {"en": 100, "ch": 120, "math": 99}, (2,'java'): 9}
#print(d.keys())
#查询
#c = d.keys()
#print(c)
#print(type(c))
#print(type(5))
#print(d.values())
#print(d.items())
#删除
#d.pop('course')
#(d)
#print(d.pop('course')) # 函数的返回值  #指定删除
# print(d.popitem())    #随机删除
#print(d.clear())
#d.clear()   #清空
#print(d)

#修改和新增

#d['class_id'] = 'JAVA'
#d['age'] = 18
#print(d)

#print(d.get('course'))   # 和 d[key]  一样的

#d[13] = 13
#d.popitem()
#print(d)

