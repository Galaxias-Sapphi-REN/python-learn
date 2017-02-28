#!/usr/bin/python
# encoding: utf-8
"""

Created on 2017-1-20

@author: sapphire

序列 是 Python 中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
列表用[ ]标识。是python最通用的复合数据类型。
列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
加号（+）是列表连接运算符，星号（*）是重复操作。
"""


# 基本操作
def base_operator():
    """
---------------------------------------------------------------------------------------------------
    例：常用的list基本操作
---------------------------------------------------------------------------------------------------
    :return:
    """
    list1 = ['physics', 'chemistry', 1997, 2000]

    print(list1)
    del list1[2]
    print("After deleting value at index 2 : ")
    print(list1)


# 脚本操作符
def script_operator():
    """
---------------------------------------------------------------------------------------------------
    例：打印常用的list脚本操作符
---------------------------------------------------------------------------------------------------
    Python表达式	                    结果	                            描述
    len([1, 2, 3])	                3	                            长度
    [1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	            组合
    ['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
    3 in [1, 2, 3]	                True	                        元素是否存在于列表中
    for x in [1, 2, 3]: print x,	1 2 3	                        迭代
---------------------------------------------------------------------------------------------------
    :return:
    """
    print('len([1, 2, 3])               : ' + str(len([1, 2, 3])))
    print('[1, 2, 3] + [4, 5, 6]        : ' + str([1, 2, 3] + [4, 5, 6]))
    print('[\'Hi!\'] * 4)               : ' + str(['Hi!'] * 4))
    print('for x in [1, 2, 3]: print(x) : ')
    for x in [1, 2, 3]:
        print(x)


# 内建函数和列表函数
def built_in_and_list_function():
    """
---------------------------------------------------------------------------------------------------
    内建函数和列表函数
---------------------------------------------------------------------------------------------------
    :return:
    """
    print ('List')
    my_list = ['runoob', 786, 2.23, 'john', 70.2]
    tiny_list = [123, 'john']

    print(str(my_list))  # 输出完整列表
    print(str(my_list[0]))  # 输出列表的第一个元素
    print(str(my_list[1:3]))  # 输出第二个至第三个的元素
    print(str(my_list[2:]))  # 输出从第三个开始至列表末尾的所有元素
    print(str(tiny_list * 2))  # 输出列表两次
    print(str(my_list + tiny_list))  # 打印组合的列表

    workday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print (workday[0:3])
    print (workday[:3])
    print (workday[-1])
    print (workday[-3:])
    print (workday[::2])
    print (workday[::-1])

    print ('Array Tuple')
    print ('Array Dictionary')

    names = ['ZhangYang', 'ZhaoYi', 'ShaoYiFan', 'JiaChen', 'MengLingJun', 'LiuLin']
    # 插入
    names.insert(2, 'YangRui')
    # 追加 this list creation could be rewritten as a list literal
    names.append('YangRui')
    # 修改
    names[2] = 'YangRui'
    # 删除
    names.remove('YangRui')
    del names[1]
    names.pop(1)
    # 索引
    names.index('YangRui')
    # 统计数量
    names.count('YangRui')
    # 清空列表
    # names.clear()
    # 反转
    names.reverse()
    # 排序
    names.sort()
    # 合并列表
    names.extend(['YangRui'])

    # 复制列表，浅copy
    names = ['ZhangYang', 'ZhaoYi', 'ShaoYiFan', 'JiaChen', 'MengLingJun', 'LiuLin', ['YangRui']]
    # names2 = names.copy()
    # print (names, names2)

    import copy
    # 复制列表，深copy
    names2 = copy.deepcopy(names)

    names[3] = '汤姆'
    names[-1][0] = '杰克'
    print (names)
    print (names2)

    # 循环列表
    for i in names:
        print (i)

    # 浅copy，3中方式
    person = ['name', ['saving', 100]]
    '''
    p1 = copy.copy(person)
    p2 = person[:]
    p3 = list(person)
    '''
    p1 = person[:]
    p2 = person[:]
    p1[0] = 'tom'
    p2[0] = 'jane'
    p1[1][1] = 50
    print (p1)
    print (p2)


print('''
===================================================================================================
=                                               Open                                              =
===================================================================================================
''')

print(__doc__)

print('''
===================================================================================================
=                                           Base Operator                                         =
===================================================================================================
''')

# 基本操作
print(base_operator.__doc__)
base_operator()

print('''
===================================================================================================
=                                          Script Operator                                        =
===================================================================================================
''')

# 脚本操作符
print(script_operator.__doc__)
script_operator()

print('''
===================================================================================================
=                                    Built-in And List Function                                   =
===================================================================================================
''')

# 内建函数和列表函数
print(built_in_and_list_function.__doc__)
built_in_and_list_function()

print('''
===================================================================================================
=                                              Closed                                             =
===================================================================================================
''')
