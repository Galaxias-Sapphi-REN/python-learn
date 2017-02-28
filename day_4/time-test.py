#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2017-1-21

@author: sapphire

Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

在Python中，通常有这几种方式来表示时间：
    1）时间戳
    2）格式化的时间字符串
    3）元组（struct_time）共九个元素。
"""

import time  # 引入time模块


# time模块 用元组（struct_time）九个元素表示时间
def struct_time():
    """
---------------------------------------------------------------------------------------------------
    例：time模块 用元组（struct_time）九个元素表示时间
---------------------------------------------------------------------------------------------------
    由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。 类型为<type 'time.struct_time'>
        UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。
        DST（Daylight Saving Time）即夏令时。

    元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。
---------------------------------------------------------------------------------------------------
    :return:
    """
    # 将一个时间戳转换为当前时区的struct_time。参数未提供，则以当前时间为准。
    print("local time from now is                   : " + str(time.localtime()))
    print("local time from 0 is                     : " + str(time.localtime(0)))

    # 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
    print("UTC time from now is                     : " + str(time.gmtime()))
    print("UTC time from 0 is                       : " + str(time.gmtime(0)))


# time模块 用时间戳表示时间
def timestamp_time():
    """
---------------------------------------------------------------------------------------------------
    例：time模块 用时间戳表示时间
---------------------------------------------------------------------------------------------------
    时间间隔是以秒为单位的`浮点小数`。
    每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。表示按秒计算的偏移量。
    Python 的 time 模块下有很多函数可以转换常见日期格式。如：
    返回时间戳方式的函数主要有time()，clock()等。
---------------------------------------------------------------------------------------------------
    :return:
    """
    # 线程推迟指定的时间运行，单位为秒。
    time.sleep(1)
    # UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。
    # 而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
    print("clock timestamp 1 is                      :   %s" % time.clock())
    time.sleep(1)
    print("clock timestamp 2 is                      :   %s" % time.clock())
    time.sleep(1)
    print("clock timestamp 3 is                      :   %s" % time.clock())

    # 返回当前时间的时间戳
    print("timestamp from now is                     : " + str(time.time()))
    # 将一个struct_time转化为时间戳。
    print("timestamp from local time struct_time is  : " + str(time.mktime(time.localtime())))


# time模块 用字符串表示时间
def string_time():
    """
---------------------------------------------------------------------------------------------------
   例：time模块 用字符串表示时间
---------------------------------------------------------------------------------------------------
   时间间隔是以秒为单位的`浮点小数`。
   每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。表示按秒计算的偏移量。
   Python 的 time 模块下有很多函数可以转换常见日期格式。如：
   返回时间戳方式的函数主要有time()，clock()等。
---------------------------------------------------------------------------------------------------
   :return:
   """
    # 把一个表示时间的元组或者struct_time表示为这种形式：'Thu Jan  1 08:00:00 1970'。如果没有参数，将会将time.localtime()作为参数传入。
    print("string time from now is                      : " + time.asctime(time.localtime(0)))
    print("string time from 0 is                        : " + time.asctime())

    # 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。
    # 它的作用相当于time.asctime(time.localtime(secs))。
    print("string time from now is                      : " + time.ctime())
    print("string time from 0 is                        : " + time.ctime(0))

    # 把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。
    # 如果元组中任何一个元素越界，ValueError的错误将会被抛出。
    # %a 本地（locale）简化星期名称
    # %A 本地完整星期名称
    # %b 本地简化月份名称
    # %B 本地完整月份名称
    # %c 本地相应的日期和时间表示
    # %d 一个月中的第几天（01 - 31）
    # %H 一天中的第几个小时（24小时制，00 - 23）
    # %I 第几个小时（12小时制，01 - 12）
    # %m 月份（01 - 12）
    # %M 分钟数（00 - 59）
    # %p 本地am或者pm的相应符
    # %S 秒（01 - 61）
    # %U 一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
    # %w 一个星期中的第几天（0 - 6，0是星期天）
    # %W 和%U基本相同，不同的是%W以星期一为一个星期的开始。
    # %x 本地相应日期
    # %y 去掉世纪的年份（00 - 99）
    # %Y 完整的年份
    # %Z 时区的名字（如果不存在为空字符）
    # %% ‘%’字符
    local_time = time.localtime()
    print("local time from now is                       : " + str(local_time))
    print("string time format is                        : " + time.strftime("%x %X", local_time))
    print("string time format is                        : " + time.strftime("%x %X", local_time))
    print("string time format is                        : " + time.strftime("%y-%m-%d %H-%M-%S", local_time))
    # CST时区2017年-第06星期-第1天-第10小时-AM-Monday-February
    print("string time format is                        : " + time.strftime("%Z时区%Y年-第%U星期-第%w天-第%I小时-%p-%A-%B",
                                                                            local_time))
    # Mon Feb  6 10:27:53 2017
    print("string time format is                        : " + time.strftime("%c", local_time))
    # 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
    print("string time format from 0 is                 : " + str(time.strptime('Thu Jan  1 08:00:00 1970', '%c')))


print('''
===================================================================================================
=                                               Open                                              =
===================================================================================================
''')

print(__doc__)

print('''
===================================================================================================
=                                            Struct Time                                          =
===================================================================================================
''')
# 用元组（struct_time）九个元素表示时间
print(struct_time.__doc__)
struct_time()
print('''
===================================================================================================
=                                           Timestamp Time                                        =
===================================================================================================
''')
# 用时间戳表示时间
print(timestamp_time.__doc__)
timestamp_time()
print('''
===================================================================================================
=                                            String Time                                          =
===================================================================================================
''')
# 用字符串表示时间
print(string_time.__doc__)
string_time()
print('''
===================================================================================================
=                                           Relationship                                          =
===================================================================================================
---------------  --> strptime   ---------------  --> localtime/gmtime   ------------------
- string_time -                 - struct_time -                         - timestamp_time -
---------------  <-- strftime   ---------------  --> mktime             ------------------
''')
print('''
===================================================================================================
=                                              Closed                                             =
===================================================================================================
''')
