#!/usr/bin/python
# encoding: utf-8
"""
Created on 2017-1-19

@author: sapphire

control flow statement~
"""


# if-elif-else基本用法
def enter_name_and_print_welcome():
    """
---------------------------------------------------------------------------------------------------
    例：输入名称，输出欢迎
---------------------------------------------------------------------------------------------------
    @Notes ：
    If you use input, then the data you type is is interpreted as a Python Expression
    which means that you end up with gawd knows what type of object in your target variable,
    and a heck of a wide range of exceptions that can be generated. So you should NOT use input
    unless you're putting something in for temporary testing, to be used only by someone
    who knows a bit about Python expressions.

    raw_input always returns a string because, heck, that's what you always type in ...
    but then you can easily convert it to the specific type you want,
    and catch the specific exceptions that may occur. Hopefully with that explanation,
    it's a no-brainer to know which you should use.
---------------------------------------------------------------------------------------------------
    :return:
    """
    print('Hello, Mr. \'True\', may i ask u to have breakfast?\n' if True else 'Suck \'False\'!\n')

    # Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

    name = raw_input("Enter \'sapphire\' or \'python\' for forecast : ").lower()
    if name == 'sapphire' or name == '':
        print('\nOh, Sapphire. Super! You will have a nice day~!@')
    elif name == 'python':
        print('\nWelcome to python.')
    else:
        print('\nOk, Good luck.' + name.capitalize())

    if True:
        print('Whether u believe it or not, this is \'True\'!')


# while基本用法
def even_and_odd_array():
    """
---------------------------------------------------------------------------------------------------
    例：分类奇数偶数
---------------------------------------------------------------------------------------------------
    @Notes ：
    list.reverse() reverses the items of s in place

    The sort() and reverse() methods modify the list in place for economy of space
    when sorting or reversing a large list. To remind you that they operate by side effect,
    they don’t return the sorted or reversed list.
---------------------------------------------------------------------------------------------------
    :return:
    """
    arr_str = str(raw_input("\nEnter a list of number with\',\' : "))
    arr_main = arr_str.split(',')
    arr_even = []
    arr__odd = []
    print('Main array is : ' + str(arr_main))
    while len(arr_main) > 0:
        num = int(arr_main.pop())
        if num % 2 == 0:
            arr_even.append(num)
        else:
            arr__odd.append(num)

        arr_even.reverse()
        arr__odd.reverse()
    print('even numbers is : ' + str(arr_even))
    print(' odd numbers is : ' + str(arr__odd))


# continue-break基本用法
def only_sort_positive():
    """
---------------------------------------------------------------------------------------------------
    例：正数排序，负数不处理，0退出 Positive and negative
---------------------------------------------------------------------------------------------------
    continue 用于跳过该次循环，break 则是用于退出循环
---------------------------------------------------------------------------------------------------
    :return:
    """
    print(" Positive to sort, negative to ignore, 0 to quit.")
    sort_list = []
    num_input = 1
    while num_input:
        num_input = input("\nEnter a number : ")
        if num_input > 0:
            sort_list.append(num_input)

    sort_list.sort()
    print(' sort list is : ' + str(sort_list))


# while-else基本用法
def calculate_factorial():
    """
---------------------------------------------------------------------------------------------------
    例：求阶乘
---------------------------------------------------------------------------------------------------
    calculates a number's factorial
---------------------------------------------------------------------------------------------------
    :return:
    """
    factorial = count = 0
    num_input = input("\nEnter a number to calculate factorial: ")
    while count < num_input:
        count += 1
        factorial += count
    else:
        print(str(count) + '\'s factorial is ： ' + str(factorial))


# for基本用法
def is_num_prime(num):
    """
---------------------------------------------------------------------------------------------------
    例：是否是质数
---------------------------------------------------------------------------------------------------
    :return:
    """
    if not isinstance(num, int):
        exit(0)
    for i in range(2, num // 2 + 1):
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            is_num_prime(j)
            print('%d = %d * %d' % (num, i, j))
            break
    else:
        print('%d is a prime number!' % num)


# for-else基本用法
def sleep_sheep(count):
    """
---------------------------------------------------------------------------------------------------
    例：数羊睡觉
---------------------------------------------------------------------------------------------------
    :return:
    """
    sleep_str = []
    for index in range(count):
        sleep_str.append('Sheep')
    else:
        sleep_str.append('Sleep')

    print(str(sleep_str).lstrip('[').rstrip(']') + "...zzZ")


# loop-loop基本用法
def print_all_prime_little_than(num):
    """
---------------------------------------------------------------------------------------------------
    例：打印比数字小的所有质数
---------------------------------------------------------------------------------------------------
    :param num:
    :return:
    """
    prime_list = []
    i = 2
    while i <= num:
        j = 2
        while j * j < i:  # 比如枚举17的因数，。因为4^2 < 17 < 5^2，所以只需要枚举2，3，4均不能被17整除，则17为质数
            if not i % j:  # 有因数
                break
            j += 1
        if j * j > i:
            prime_list.append(i)
        i += 1
    print('prime nums : ' + str(prime_list).lstrip('[').rstrip(']'))


# break-continue-pass基本用法
def break_up_word(word):
    """
---------------------------------------------------------------------------------------------------
    例：拆散单词，若字母
---------------------------------------------------------------------------------------------------
        p：pass
        b：break
        c：continue
---------------------------------------------------------------------------------------------------
    :param word:
    :return:
    """
    word_list = []
    print(word.ljust(25, '~'))
    for letter in word:
        if letter.lower() == 'p':
            print('P~~~~~~~')
            pass
            print('ass!')
        if letter.lower() == 'b':
            print('B~~~~~~~no~reak!')
            break
        if letter.lower() == 'c':
            print('C~~~~~~~no~ontinue!')
            continue
        word_list.append(letter)
    print(str(word_list).lstrip('[').rstrip(']'))


print(__doc__)
print('''
===================================================================================================
=                                       Conditional Statements                                    =
===================================================================================================
''')
# 输入名称，输出欢迎
print(enter_name_and_print_welcome.__doc__)
enter_name_and_print_welcome()
print('''
===================================================================================================
=                                          Loop Statements                                        =
===================================================================================================
''')
# 分类奇数偶数
print(even_and_odd_array.__doc__)
even_and_odd_array()
# 正数排序，负数不处理，0退出
print(only_sort_positive.__doc__)
only_sort_positive()
# 求阶乘
print(calculate_factorial.__doc__)
calculate_factorial()
# 是否是质数
print(is_num_prime.__doc__)
is_num_prime(49)
# 数羊睡觉
print(sleep_sheep.__doc__)
sleep_sheep(10)
# 打印比数字小的所有质数
print(print_all_prime_little_than.__doc__)
print_all_prime_little_than(50)
# 拆散单词
print(break_up_word.__doc__)
break_up_word('picture boom!')
print('''
===================================================================================================
=                                               Closed                                            =
===================================================================================================
''')
