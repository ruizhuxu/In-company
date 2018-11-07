# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 16:21
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : function2_printCalendar.py
# @Software: PyCharm
'''
输入一个年和月，判断距离1800年1月1号到现在的1号多少天，输入的1号是星期几
'''
def is_leap_year(year):          # 判断年是不是闰年
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_num_of_days_in_month(year,month):  # 获得月份的天数
    # if month == 1 or month == 3 or  month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_total_num_of_days(year,month):  # 获得距离1800年的天数
    days = 0
    for y in range(1800,year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    for m in range(1,month):
        days += get_num_of_days_in_month(year,m)
    return days

def get_start_day(year,month):         #
    return (3 + get_total_num_of_days(year,month)) % 7  # 1800年1月1号是星期三

def main():
    year = eval(input("请输入一个年份："))
    month = eval(input("请输入一个月份："))
    print("{}年{}月1号是星期{}".format(year,month,get_start_day(year,month)))
main()

