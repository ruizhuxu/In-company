# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 17:14
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : function3_recursive_n_factorial.py
# @Software: PyCharm

# n的阶乘

'''
def p(n):
    x = 1
    i = n
    while i >= 1:
        x = x * i
        i = i - 1
    return x
print(p(3))
'''
'''
def p(n):
    x = 1
    i = 1
    while i <= n:
        x = x * i
        i = i + 1
    return x
'''

def p(n):  # 使用递归，n！= n * （n-1）！
    if n == 1 or n == 0:
        return 1
    else:
        return p(n-1)*n

print(p(5))
