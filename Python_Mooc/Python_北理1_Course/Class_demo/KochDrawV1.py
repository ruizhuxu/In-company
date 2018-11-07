# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 16:36
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : KochDrawV1.py
# @Software: PyCharm

#KochDrawV1.py  科赫雪花的绘制

import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
def main():
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    level = 3
    koch(400,level)
    t.right(120)
    koch(400, level)
    t.right(120)
    koch(400, level)
    t.hideturtle()
main()




