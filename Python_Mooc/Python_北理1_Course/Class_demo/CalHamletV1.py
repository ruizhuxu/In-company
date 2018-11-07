# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 12:00
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : CalHamletV1.py
# @Software: PyCharm

def getText():
    txt = open("").read()
    txt = txt.lower()

    return

hamletTxt = getText()
words = hamletTxt.split()   # words 是一个列表
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1

