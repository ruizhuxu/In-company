# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 16:36
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : KochDrawV1.py
# @Software: PyCharm

#KochDrawV1.py

import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main():
    t.setup(800,400)
    t.penup()
    t.goto(-300,-50)
    t.pendown()
    t.pensize(2)
    koch(600,2)   #2阶科赫曲线
    t.hideturtle()
main()




