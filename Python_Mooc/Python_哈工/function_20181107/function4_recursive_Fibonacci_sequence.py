# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 17:37
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : function4_recursive_Fibonacci_sequence.py
# @Software: PyCharm

'''
小兔子长大，生小兔子,小兔子长大，生小兔子的故事......
斐波那契数列：1,1,2,3,5,8,13,21,34,55,89......
n=1, f(n)=1
n=2, f(n)=1
n>2, f(n)=f(n-1)+f(n-2)
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(11))
