#!/usr/bin/env python
# encoding: utf-8
"""
Created on 2017-1-20

@author: sapphire

Python Number 数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。
"""

import math
import random


# 数值类型
def number_type():
    """
---------------------------------------------------------------------------------------------------
    例：打印一些支持的数值类型
---------------------------------------------------------------------------------------------------
    @Note:
    整型丶     (Int)                           - 通常被称为是整型或整数，是正或负整数，不带小数点。
    长整型     (long integers)                 - 无限大小的整数，整数最后是一个大写或小写的L。
    浮点型     (floating point real values)    - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    复数丶     (complex numbers)               - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
---------------------------------------------------------------------------------------------------
    :return:
    """
    # 在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647
    # 在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807
    print('[  int      ]', 10, 100, -786, 80, -0b1100, -0xfff, 0o77,
          -2 ** 62 - 4611686018427387904, 2 ** 62 + 4611686018427387903)
    print('[  long     ]', 9223372036854775807 + 1, -9223372036854775808 - 1, 1L)
    print('[  float    ]', 0.0, 15.20, -21.9, 32.3e18, -90., -32.54e-100, 70.2E-12)
    print('[  complex  ]', 3.14j, 45.j, 9.322e-36j, .876j, -.6545 + 0J, 3e+26J, 4.53e-7j)


# 类型转换
def convert(msg_param):
    """
---------------------------------------------------------------------------------------------------
    例：打印一些基本的类型转换
---------------------------------------------------------------------------------------------------
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
---------------------------------------------------------------------------------------------------
    函数	                                        描述
    int(x [,base])                              将x转换为一个整数
    long(x [,base] )                            将x转换为一个长整数
    float(x)                                    将x转换到一个浮点数
    complex(real [,imag])                       创建一个复数
    str(x)                                      将对象 x 转换为字符串
    repr(x)                                     将对象 x 转换为表达式字符串
    eval(str)                                   用来计算在字符串中的有效Python表达式,并返回一个对象
    tuple(s)                                    将序列 s 转换为一个元组
    list(s)                                     将序列 s 转换为一个列表
    set(s)                                      转换为可变集合
    dict(d)                                     创建一个字典。d 必须是一个序列 (key,value)元组。
    frozenset(s)                                转换为不可变集合
    chr(x)                                      将一个整数转换为一个字符
    unichr(x)                                   将一个整数转换为Unicode字符
    ord(x)                                      将一个字符转换为它的整数值
    hex(x)                                      将一个整数转换为一个十六进制字符串
    oct(x)                                      将一个整数转换为一个八进制字符串
--------------------------------------------------------------------------------------------
    :param msg_param:
    :return:
    """
    msg = str(msg_param)
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
str is : ''' + msg)
    if msg.isdigit():
        print('float is :'.ljust(20, ' ') + str(float(msg)))
        print('complex is :'.ljust(20, ' ') + str(complex(msg)))
        # ValueError: substring not found
        if msg.find('.') > 0:
            print('int is :'.ljust(20, ' ') + str(int(msg)))
            print('long is :'.ljust(20, ' ') + str(long(msg)))
            print('ord is :'.ljust(20, ' ') + str(ord(msg)))
            # TypeError: an integer is required
            print('chr is :'.ljust(20, ' ') + str(chr(int(msg))))
            print('unichr is :'.ljust(20, ' ') + str(unichr(int(msg))))
            # TypeError: hex() argument can't be converted to hex
            print('hex is :'.ljust(20, ' ') + str(hex(msg)))
            print('oct is :'.ljust(20, ' ') + oct(hex(msg)))
    else:
        print('repr is :'.ljust(20, ' ') + str(repr(msg)))
        print('tuple is :'.ljust(20, ' ') + str(tuple(msg)))
        print('list is :'.ljust(20, ' ') + str(list(msg)))
        print('set is :'.ljust(20, ' ') + str(set(msg)))
        # {'name': 'john', 'code': 6734, 'dept': 'sales'}
        # ValueError: dictionary update sequence element #0 has length 1; 2 is required
        print('dict is :'.ljust(20, ' ') + str(dict({'msg': msg, 'any': 1})))
        print('frozenset is :'.ljust(20, ' ') + str(frozenset(msg)))


# 数学函数
def base_math_function_of_number():
    """
---------------------------------------------------------------------------------------------------
    例：打印一些基本的操作函数
---------------------------------------------------------------------------------------------------
    函数	                返回值 ( 描述 )
    abs(x)	            返回数字的绝对值，如abs(-10) 返回 10
    ceil(x)	            返回数字的上入整数，如math.ceil(4.1) 返回 5
    cmp(x, y)	            如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
    exp(x)	            返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    fabs(x)	            返回数字的绝对值，如math.fabs(-10) 返回10.0
    floor(x)	        返回数字的下舍整数，如math.floor(4.9)返回 4
    log(x)	            如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    log10(x)	        返回以10为基数的x的对数，如math.log10(100)返回 2.0
    max(x1, x2,...)	    返回给定参数的最大值，参数可以为序列。
    min(x1, x2,...)	    返回给定参数的最小值，参数可以为序列。
    modf(x)	            返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    pow(x, y)	x**y    运算后的值。
    round(x [,n])	    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
    sqrt(x)	            返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
    :return:
    """
    var1 = 1
    del var1
    # UnboundLocalError: local variable 'var1' referenced before assignment
    # print("del data : ".rjust(30, ' ') + var1)
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 绝对值
''')
    print("\tabs(-45) : ".ljust(30, ' ') + str(abs(-45)))
    print("\tabs(100.12) : ".ljust(30, ' ') + str(abs(100.12)))
    print("\tabs(119L) : ".ljust(30, ' ') + str(abs(119L)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 向上取整
''')
    print("\tmath.ceil(1) : ".ljust(30, ' ') + str(math.ceil(1)))
    print("\tmath.ceil(-45.17) : ".ljust(30, ' ') + str(math.ceil(-45.17)))
    print("\tmath.ceil(100.12) : ".ljust(30, ' ') + str(math.ceil(100.12)))
    print("\tmath.ceil(100.72) : ".ljust(30, ' ') + str(math.ceil(100.72)))
    print("\tmath.ceil(119L) : ".ljust(30, ' ') + str(math.ceil(119L)))
    print("\tmath.ceil(math.pi) : ".ljust(30, ' ') + str(math.ceil(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   # 比较大小
''')
    print("\tcmp(80, 100) : ".ljust(30, ' ') + str(cmp(80, 100)))
    print("\tcmp(180, 100) : ".ljust(30, ' ') + str(cmp(180, 100)))
    print("\tcmp(-80, 100) : ".ljust(30, ' ') + str(cmp(-80, 100)))
    print("\tcmp(80, -100) : ".ljust(30, ' ') + str(cmp(80, -100)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # e的指数
''')
    print("\tmath.exp(1) : ".ljust(30, ' ') + str(math.exp(1)))
    print("\tmath.exp(-45.17) : ".ljust(30, ' ') + str(math.exp(-45.17)))
    print("\tmath.exp(100.12) : ".ljust(30, ' ') + str(math.exp(100.12)))
    print("\tmath.exp(100.72) : ".ljust(30, ' ') + str(math.exp(100.72)))
    print("\tmath.exp(119L) : ".ljust(30, ' ') + str(math.exp(119L)))
    print("\tmath.exp(math.pi) : ".ljust(30, ' ') + str(math.exp(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # float绝对值
''')
    print("\tmath.fabs(-45.17) : ".ljust(30, ' ') + str(math.fabs(-45.17)))
    print("\tmath.fabs(100.12) : ".ljust(30, ' ') + str(math.fabs(100.12)))
    print("\tmath.fabs(100.72) : ".ljust(30, ' ') + str(math.fabs(100.72)))
    print("\tmath.fabs(119L) : ".ljust(30, ' ') + str(math.fabs(119L)))
    print("\tmath.fabs(math.pi) : ".ljust(30, ' ') + str(math.fabs(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 向下取整
''')
    print("\tmath.floor(-45.17) : ".ljust(30, ' ') + str(math.floor(-45.17)))
    print("\tmath.floor(100.12) : ".ljust(30, ' ') + str(math.floor(100.12)))
    print("\tmath.floor(100.72) : ".ljust(30, ' ') + str(math.floor(100.72)))
    print("\tmath.floor(119L) : ".ljust(30, ' ') + str(math.floor(119L)))
    print("\tmath.floor(math.pi) : ".ljust(30, ' ') + str(math.floor(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # x的自然对数
''')
    print("\tmath.log(100.12) : ".ljust(30, ' ') + str(math.log(100.12)))
    print("\tmath.log(100.72) : ".ljust(30, ' ') + str(math.log(100.72)))
    print("\tmath.log(119L) : ".ljust(30, ' ') + str(math.log(119L)))
    print("\tmath.log(math.pi) : ".ljust(30, ' ') + str(math.log(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 10为基数的x对数
''')
    print("\tmath.log10(100.12) : ".ljust(30, ' ') + str(math.log10(100.12)))
    print("\tmath.log10(100.72) : ".ljust(30, ' ') + str(math.log10(100.72)))
    print("\tmath.log10(119L) : ".ljust(30, ' ') + str(math.log10(119L)))
    print("\tmath.log10(math.pi) : ".ljust(30, ' ') + str(math.log10(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 最大值
''')
    print("\tmax(80, 100, 1000) : ".ljust(30, ' ') + str(max(80, 100, 1000)))
    print("\tmax(-20, 100, 400) : ".ljust(30, ' ') + str(max(-20, 100, 400)))
    print("\tmax(-80, -20, -10) : ".ljust(30, ' ') + str(max(-80, -20, -10)))
    print("\tmax(0, 100, -400) : ".ljust(30, ' ') + str(max(0, 100, -400)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 最小值
''')
    print("\tmin(80, 100, 1000) : ".ljust(30, ' ') + str(min(80, 100, 1000)))
    print("\tmin(-20, 100, 400) : ".ljust(30, ' ') + str(min(-20, 100, 400)))
    print("\tmin(-80, -20, -10) : ".ljust(30, ' ') + str(min(-80, -20, -10)))
    print("\tmin(0, 100, -400) : ".ljust(30, ' ') + str(min(0, 100, -400)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
''')
    print("\tmath.modf(100.12) : ".ljust(30, ' ') + str(math.modf(100.12)))
    print("\tmath.modf(100.72) : ".ljust(30, ' ') + str(math.modf(100.72)))
    print("\tmath.modf(119L) : ".ljust(30, ' ') + str(math.modf(119L)))
    print("\tmath.modf(math.pi) : ".ljust(30, ' ') + str(math.modf(math.pi)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # x的y次方
''')
    print("\tmath.pow(100, 2) : ".ljust(30, ' ') + str(math.pow(100, 2)))
    # 使用内置，查看输出结果区别
    print("\tpow(100, 2) : ".ljust(30, ' ') + str(pow(100, 2)))

    print("\tmath.pow(100, -2) : ".ljust(30, ' ') + str(math.pow(100, -2)))
    print("\tmath.pow(2, 4) : ".ljust(30, ' ') + str(math.pow(2, 4)))
    print("\tmath.pow(3, 0) : ".ljust(30, ' ') + str(math.pow(3, 0)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 四舍五入
''')
    print("\tround(80.23456, 2) : ".ljust(30, ' ') + str(round(80.23456, 2)))
    print("\tround(100.000056, 3) : ".ljust(30, ' ') + str(round(100.000056, 3)))
    print("\tround(-100.000056, 3) : ".ljust(30, ' ') + str(round(-100.000056, 3)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 平方根
''')
    print("\tmath.sqrt(100) : ".ljust(30, ' ') + str(math.sqrt(100)))
    print("\tmath.sqrt(7) : ".ljust(30, ' ') + str(math.sqrt(7)))
    print("\tmath.sqrt(math.pi) : ".ljust(30, ' ') + str(math.sqrt(math.pi)))


# 随机数函数
def random_number():
    """
---------------------------------------------------------------------------------------------------
    例：随机数函数
---------------------------------------------------------------------------------------------------
    随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
---------------------------------------------------------------------------------------------------
    函数	                                描述
    choice(seq)	                        从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
    random()	                        随机生成下一个实数，它在[0,1)范围内。
    seed([x])	                        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    shuffle(lst)	                    将序列的所有元素随机排序
    uniform(x, y)	                    随机生成下一个实数，它在[x,y]范围内。
---------------------------------------------------------------------------------------------------

    :return:
    """
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # choice 列表，元组或字符串的随机项。
''')
    print("\tchoice([1, 2, 3, 5, 9]) : ".ljust(30, ' ') + str(random.choice([1, 2, 3, 5, 9])))
    print("\tchoice('A String') : ".ljust(30, ' ') + str(random.choice('A String')))
    print("\tchoice(range(10)) : ".ljust(30, ' ') + str(random.choice(range(10))))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # randrange 递增基数集合中的一个随机数，基数缺省值为1。
''')
    print("\trandrange(100, 1000) : ".ljust(30, ' ') + str(random.randrange(100, 1000)))
    # ValueError: non-integer arg 1 for randrange()
    # print("\trandrange(100.1, 1000) : ".ljust(30, ' ') + str(random.randrange(100.1, 1000)))
    # 输出 100 <= number < 1000 间的偶数
    print("\trandrange(100, 1000, 2) : ".ljust(30, ' ') + str(random.randrange(100, 1000, 2)))
    # 输出 100 <= number < 1000 间的其他数
    print("\trandrange(100, 1000, 3) : ".ljust(30, ' ') + str(random.randrange(100, 1000, 3)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # random 随机生成的一个实数，它在[0,1)范围内。
''')
    # 生成第一个随机数
    print("\trandom() : ".ljust(30, ' ') + str(random.random()))
    # 生成第二个随机数
    print("\trandom() : ".ljust(30, ' ') + str(random.random()))
    print("\trandom() : ".ljust(30, ' ') + str(int(random.random() * 100)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # seed 改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
''')
    random.seed(10)
    print("\tRandom number with seed 10 : ".ljust(30, ' ') + str(random.random()))

    # 生成同一个随机数
    random.seed(10)
    print("\tRandom number with seed 10 : ".ljust(30, ' ') + str(random.random()))

    # 生成同一个随机数
    random.seed(10)
    print("\tRandom number with seed 10 : ".ljust(30, ' ') + str(random.random()))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # shuffle 将序列的所有元素随机排序。
''')
    my_list = [20, 16, 10, 5]
    random.shuffle(my_list)
    print("\t随机排序列表 : ".ljust(30, ' ') + str(my_list))

    random.seed()
    random.shuffle(my_list)
    print("\t随机排序列表 : ".ljust(30, ' ') + str(my_list))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # uniform 随机生成下一个实数，它在[x,y]范围内。
''')
    print("\tuniform(5, 10) 的随机数为 : ".ljust(30, ' ') + str(random.uniform(5, 10)))

    print("\tuniform(7, 14) 的随机数为 : ".ljust(30, ' ') + str(random.uniform(7, 14)))


# 三角函数
def trigonometric_function():
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # acos 反余弦弧度值
''')
    print("\tacos(0.64) : ".ljust(30, ' ') + str(math.acos(0.64)))
    print("\tacos(0) : ".ljust(30, ' ') + str(math.acos(0)))
    print("\tacos(-1) : ".ljust(30, ' ') + str(math.acos(-1)))
    print("\tacos(1) : ".ljust(30, ' ') + str(math.acos(1)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # asin 反正弦弧度值
''')
    print("\tasin(0.64) : ".ljust(30, ' ') + str(math.asin(0.64)))
    print("\tasin(0) : ".ljust(30, ' ') + str(math.asin(0)))
    print("\tasin(-1) : ".ljust(30, ' ') + str(math.asin(-1)))
    print("\tasin(1) : ".ljust(30, ' ') + str(math.asin(1)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # atan 反正切弧度值
''')
    print("\tatan(0.64) : ".ljust(30, ' ') + str(math.atan(0.64)))
    print("\tatan(0) : ".ljust(30, ' ') + str(math.atan(0)))
    print("\tatan(10) : ".ljust(30, ' ') + str(math.atan(10)))
    print("\tatan(-1) : ".ljust(30, ' ') + str(math.atan(-1)))
    print("\tatan(1) : ".ljust(30, ' ') + str(math.atan(1)))
    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # atan2 X 及 Y 坐标值的反正切值
''')
    print("\tatan2(-0.50,-0.50) : ".ljust(30, ' ') + str(math.atan2(-0.50, -0.50)))
    print("\tatan2(0.50,0.50) : ".ljust(30, ' ') + str(math.atan2(0.50, 0.50)))
    print("\tatan2(5,5) : ".ljust(30, ' ') + str(math.atan2(5, 5)))
    print("\tatan2(-10,10) : ".ljust(30, ' ') + str(math.atan2(-10, 10)))
    print("\tatan2(10,20) : ".ljust(30, ' ') + str(math.atan2(10, 20)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # cos 余弦值
''')
    print("\tcos(3) : ".ljust(30, ' ') + str(math.cos(3)))
    print("\tcos(-3) : ".ljust(30, ' ') + str(math.cos(-3)))
    print("\tcos(0) : ".ljust(30, ' ') + str(math.cos(0)))
    print("\tcos(math.pi) : ".ljust(30, ' ') + str(math.cos(math.pi)))
    print("\tcos(2*math.pi) : ".ljust(30, ' ') + str(math.cos(2 * math.pi)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # hypot 欧几里德范数 sqrt(x*x + y*y)
''')
    print("\thypot(3, 4) : ".ljust(30, ' ') + str(math.hypot(3, 4)))
    print("\thypot(-3, 3) : ".ljust(30, ' ') + str(math.hypot(-3, 3)))
    print("\thypot(0, 2) : ".ljust(30, ' ') + str(math.hypot(0, 2)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # sin 正弦值
''')
    print("\tsin(3) : ".ljust(30, ' ') + str(math.sin(3)))
    print("\tsin(-3) : ".ljust(30, ' ') + str(math.sin(-3)))
    print("\tsin(0) : ".ljust(30, ' ') + str(math.sin(0)))
    print("\tsin(math.pi) : ".ljust(30, ' ') + str(math.sin(math.pi)))
    print("\tsin(math.pi/2) : ".ljust(30, ' ') + str(math.sin(math.pi/2)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # tan 正弦值
''')
    print("\ttan(3) : ".ljust(30, ' ') + str(math.tan(3)))
    print("\ttan(-3) : ".ljust(30, ' ') + str(math.tan(-3)))
    print("\ttan(0) : ".ljust(30, ' ') + str(math.tan(0)))
    print("\ttan(math.pi) : ".ljust(30, ' ') + str(math.tan(math.pi)))
    print("\ttan(math.pi/2) : ".ljust(30, ' ') + str(math.tan(math.pi / 2)))
    print("\ttan(math.pi/4) : ".ljust(30, ' ') + str(math.tan(math.pi / 4)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # degrees 弧度转换为角度
''')
    print("\tdegrees(3) : ".ljust(30, ' ') + str(math.degrees(3)))
    print("\tdegrees(-3) : ".ljust(30, ' ') + str(math.degrees(-3)))
    print("\tdegrees(0) : ".ljust(30, ' ') + str(math.degrees(0)))
    print("\tdegrees(math.pi) : ".ljust(30, ' ') + str(math.degrees(math.pi)))
    print("\tdegrees(math.pi/2) : ".ljust(30, ' ') + str(math.degrees(math.pi / 2)))
    print("\tdegrees(math.pi/4) : ".ljust(30, ' ') + str(math.degrees(math.pi / 4)))

    print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # radians 角度转换为弧度
''')
    print("\tradians(3) : ".ljust(30, ' ') + str(math.radians(3)))
    print("\tradians(-3) : ".ljust(30, ' ') + str(math.radians(-3)))
    print("\tradians(0) : ".ljust(30, ' ') + str(math.radians(0)))
    print("\tradians(math.pi) : ".ljust(30, ' ') + str(math.radians(math.pi)))
    print("\tradians(math.pi/2) : ".ljust(30, ' ') + str(math.radians(math.pi / 2)))
    print("\tradians(math.pi/4) : ".ljust(30, ' ') + str(math.radians(math.pi / 4)))


print('''
===================================================================================================
=                                               Open                                              =
===================================================================================================
''')

print(__doc__)

print('''
===================================================================================================
=                                           Number Type                                           =
===================================================================================================
''')

# 数值类型
print(number_type.__doc__)
number_type()

print('''
===================================================================================================
=                                            Type Cast                                            =
===================================================================================================
''')

# 类型转换
print(convert.__doc__)
convert(4)
convert(4.4)
convert('m')

print('''
===================================================================================================
=                                          Math Function                                          =
===================================================================================================
''')

# 数学函数
print(base_math_function_of_number.__doc__)
base_math_function_of_number()

print('''
===================================================================================================
=                                             Random                                              =
===================================================================================================
''')

# 随机数函数
print(random_number.__doc__)
random_number()

print('''
===================================================================================================
=                                      Trigonometric Function                                     =
===================================================================================================
''')

# 三角函数
print(trigonometric_function.__doc__)
trigonometric_function()

print('''
===================================================================================================
=                                      Mathematical Constants                                     =
===================================================================================================
''')

# 数学常量
print(math.pi)
print(math.e)

print('''
===================================================================================================
=                                               Closed                                            =
===================================================================================================
''')