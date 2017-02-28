#!/usr/local/env python
# encoding:utf-8
"""
Created on 2017-1-19

@author: sapphire
"""
from getpass import getpass

print("""
1、使用while循环输出1 2 3 4 5 6 8 9 10。
""")


def demo_1():
    loop_str = ''
    i = 0
    while i < 10:
        i += 1
        loop_str += (str(i) + ',')
    print('loop is : ' + loop_str.rstrip(','))


demo_1()
print("""
2、求1—100的所有整数的和。
""")


def demo_2():
    i = 0
    sum_num = 0
    sum_str = ''
    while i < 100:
        i += 1
        sum_num += i
        sum_str += ('+' + str(i))
    print(sum_str.lstrip('+') + '=' + str(sum_num))


demo_2()
print("""
3、输出1—100内的所有奇数。
""")


def demo_3():
    result = []
    i = 0
    while i < 100:
        i += 1
        if i % 2:
            result.append(i)
    print('even are : ' + str(result).lstrip('[').rstrip(']'))


demo_3()
print("""
4、输出1—100内的所有偶数。
""")


def demo_4():
    result = []
    i = 0
    while i < 100:
        i += 1
        if not i % 2:
            result.append(i)
    print('odd are : ' + str(result).lstrip('[').rstrip(']'))


demo_4()
print("""
5、求1-2+3-4+5 … 99的所有数的和。
""")


def demo_5():
    result_str = ''
    result = 0
    i = 0
    while i < 99:
        i += 1
        if i % 2:
            result_str += '+' + str(i)
            result += i
        else:
            result_str += '-' + str(i)
            result -= i
    print(result_str.lstrip('+') + '=' + str(result))


demo_5()
print("""
6、用户登陆连续输出密码三次锁定该用户。
""")


def demo_6():
    print('\'password : sapphire\'')
    i = 3
    log_in = False
    while i > 0:
        pwd = getpass("Enter your password : ")
        i -= 1
        if pwd.lower() == 'sapphire':
            log_in = True

            break
        else:
            print("error!(" + str(i) + ' chance!)')
    if log_in:
        print('log in! welcome sapphire.')
    else:
        print('sorry.')


demo_6()
