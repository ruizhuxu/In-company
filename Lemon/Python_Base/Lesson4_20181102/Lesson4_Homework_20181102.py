# -*- coding: utf-8 -*-
# @Time     : 2018/11/2/23:58
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson4_Homework_20181102.py
# @Software : PyCharm

'''
有一个字典：{"广东":["深圳","广州","阳江"],"湖南":["长沙","益阳","怀化"],"湖北": ["武汉","襄阳","黄冈"]}
你从控制台输入一个省份，根据你的判断，你可以选择哪些城市
当你选择完毕后，就打印一个信息到控制台，告诉你，你选择了XX省份XX城市
如果省份不存在，或者是城市不存在，那么就告诉你，你输入错误，终止程序
'''

d = {"广东":["深圳","广州","阳江"],"湖南":["长沙","益阳","怀化"],"湖北": ["武汉","襄阳","黄冈"]}

pro = input("请输入一个省份：")
if pro in d.keys():
    city = input("请选择一个城市{}：".format(d[pro]))
    if city in d[pro]:
            print("你输入了{}省{}市".format(pro, city))
    else:
        print("输入城市错误")
else:
    print("输入省份错误")








