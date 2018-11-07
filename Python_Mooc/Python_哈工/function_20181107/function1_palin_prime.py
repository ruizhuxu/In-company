# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 16:13
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : function1_palin_prime.py
# @Software: PyCharm

"""
判断一个数同时是回文数和素数
"""
num = eval(input("请输入一个整数："))
def is_palin(num): #是不是回文数
    num_p = 0
    num_t = num
    while num_t != 0:
        num_p = num_p * 10 + num_t %10
        num_t = num_t /10
    if num == num_p:
        return True
    else:
        return False

def is_prime(num):   #是不是素数
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

if is_palin(num) and is_prime(num):
    print('OK')
else:
    print('NO')
