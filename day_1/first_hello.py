#!/usr/bin/python
# encoding: utf-8
"""
Created on 2017-1-18

@author: sapphire
"""
print('\ncoding support Chinese')

# hello world
print('\nhello world')
print("\n\nwelcome to python 2.7, write by Guido van Rossum")

# escape and print line
print('\nescape and print line')
print('''\\n
        line1
        line2
        line3\n''')

# variable and no const
'''
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个``空间``。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
'''
print('\nvariable and no const')
name1 = name2 = 'Tom'
print(name1, ' ', name2)
name1 = 'Jerry'
print(name1, ' ', name2)

# interactive
print('\ninteractive')
user_name = input('please enter your \"name\" : ')
age = input('please enter your \"age\" : ')
print(' hello, ', user_name, 'i know your age is : ', age)
if int(age) >= 18:
    print('Yeah, adult, u look great!\n')
else:
    print('Young man, never say no!\n')

# process
print('\nprocess')
print('Hello, Mr. \'True\', may i ask u to have breakfast?' if True else 'Suck \'False\'!')
if True:
    print('Whether u believe it or not, this is \'True\'!')
while False:
    print('Never see me! \'False\'!')
while True:
    print('But me! \'True\'!')
    break
print('yeah! now across the world~!@')
for i in range(5):
    print('Five rabbits are staring at u : ', i)
print('on, God GeGe!')

# import modules
print('\nimport some modules')

import sys

print({sys.version})  # 打印环境变量
# print {sys.argv}                      # 打印相对路径

import os

os.system('ls')  # 执行命令不保存结果
cmd_res = os.popen('ls').read()
# os.mkdir('new_dir')                   # 创建单个目录
# os.removedirs('new_dir')              # 删除目录

# pyc
print('''
Do u know ? 当Python程序运行时，编译结果保持到内存中的pycodeobject中，当Python结束时Python解释器则将
pycodeobject写入到pyc文件中，当Python程序第二次运行时，首先程序会在硬盘中找pyc文件并和py文
件的生成时间做比对，如果pyc时间为最新时间，则直接载入，否则重复执行上面的过程''')

# data_type
print('\nNow, open the door of Data Type in python.')

print('Boolean True is 1, False is 0.')
print(True, False, True and True, not False)

print('Bytes')
msg = '(｡･ω･｡)ﾉ'
reload(sys)
print(msg.encode('utf-8'))
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xef in position 1: ordinal not in range(128)
msg = '(\xef\xbd\xa1\xef\xbd\xa5\xcf\x89\xef\xbd\xa5\xef\xbd\xa1)\xef\xbe\x89'
print(msg.decode('utf-8'))

print(None)
print(str(1), int("1"), float(1))
'''
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
'''
print(' math is 100.0 + 0xff + 1.23e1 =', 100.0 + 0xff + 1.23e1)
PI = 3.14159265359
print('10/PI=', 10 / PI)

print("\nuse DocStrings write helper!")


# DocStrings
def doc():
    """
    U never know what will happen during this method, my boy.
    print the line to show how stupid(may.be. clever :P) you are !!!

    I am DocStrings ! -> 在函数的第一个逻辑行的字符串是这个函数的 文档字符串
    """
    print('good luck!')

    '''
    Bye bye! I am not DocStrings !
    '''

    print('see you again!')
    pass


doc()
print(doc.__doc__)
help(doc)
