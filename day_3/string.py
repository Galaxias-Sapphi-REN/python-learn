#!/usr/bin/env python
# encoding: utf-8
"""
Created on 2017-1-21

@author: sapphire

字符串或串(String)是由数字、字母、下划线组成的一串字符。它是编程语言中表示文本的数据类型。
python的字串列表有2种取值顺序:
1.从左到右索引默认0开始的，最大范围是字符串长度少1
2.从右到左索引默认-1开始的，最大范围是字符串开头
如果你的实要取得一段子串的话，可以用到变量[头下标:尾下标]，就可以截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
"""


# 转义字符
def escape_character():
    """
---------------------------------------------------------------------------------------------------
    例：打印常用的转义字符
---------------------------------------------------------------------------------------------------
    :return:
    """
    print(' use \'\\\' to escape characters')
    print(' \'\\\'在行尾时:续行符 \
          another line.')
    print('反斜杠符号                    \\')
    print('单引号丶丶                    \'')
    print('双引号丶丶                    \"')
    print('响铃丶丶丶                    \a')
    print('退格丶丶丶                    \b')
    print('转义丶丶丶                    \e')
    print('空丶丶丶丶                    \000')
    print('换行丶丶丶                    \n')
    print('纵向制表符                    \v')
    print('横向制表符                    \t')
    print('回车丶丶丶                    \r')
    print('换页丶丶丶                    \f')
    print('八进制数丶                    \o12')
    print('十六进制数                    \x0a')
    print('普通格式丶                    \other')


# 字符串运算符
def string_operator(a, b):
    """
---------------------------------------------------------------------------------------------------
    例：使用常用的字符串运算符
---------------------------------------------------------------------------------------------------
    操作符	描述
    +	    字符串连接
    *	    重复输出字符串
    []	    通过索引获取字符串中字符
    [ : ]	截取字符串中的一部分
    in	    成员运算符 - 如果字符串中包含给定的字符返回 True
    not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
    r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
            原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
    %	    格式字符串
---------------------------------------------------------------------------------------------------
    :return:
    """
    print("a + b 输出结果：", a + b)
    print("a * 2 输出结果：", a * 2)
    print("a[1] 输出结果：", a[1])
    print("a[1:4] 输出结果：", a[1:4])

    if "H" in a:
        print("H 在变量 a 中")
    else:
        print("H 不在变量 a 中")

    if "M" not in a:
        print("M 不在变量 a 中")
    else:
        print("M 在变量 a 中")

    print(r'\n')
    print(R'\n')


# 字符串格式化
def string_format():
    """
---------------------------------------------------------------------------------------------------
    例：使用常用的字符串格式化
---------------------------------------------------------------------------------------------------
    Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
    但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
    在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
---------------------------------------------------------------------------------------------------
        符号	    描述
        %c	    格式化字符及其ASCII码
        %s	    格式化字符串
        %d	    格式化整数
        %u	    格式化无符号整型
        %o	    格式化无符号八进制数
        %x	    格式化无符号十六进制数
        %X	    格式化无符号十六进制数（大写）
        %f	    格式化浮点数字，可指定小数点后的精度
        %e	    用科学计数法格式化浮点数
        %E	    作用同%e，用科学计数法格式化浮点数
        %g	    %f和%e的简写
        %G	    %f和%E的简写
        %p	    用十六进制数格式化变量的地址

        符号	    功能
        *	    定义宽度或者小数点精度
        -	    用做左对齐
        +	    在正数前面显示加号( + )
        <sp>	在正数前面显示空格
        #	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
        0	    显示的数字前面填充'0'而不是默认的空格
        %	    '%%'输出一个单一的'%'
        (var)	映射变量(字典参数)
        m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

    :return:
    """

    print("My name is %s and age is %d kg!" % ('Sapphire', 24))


# 字符串内建函数
def string_build_in_function():
    """
---------------------------------------------------------------------------------------------------
    例：使用常用的字符串内建函数
---------------------------------------------------------------------------------------------------
    这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，
    所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。
---------------------------------------------------------------------------------------------------
    Summary : method
        CODE :
            decode encode
        FORMART :
            capitalize center format ljust rjust lower upper strip lstrip rstrip swapcase title zfill
        SPLIT :
            split splitlines partition rpartition
        JUDGE :
            isalnum isalpha isdigit islower isupper isspace istitle join
        FIND :
            find index rfind
        REPLACE :
            replace
---------------------------------------------------------------------------------------------------
    :return:
    """
    msg = "let\'s handle \'string\' in python 2.7! 舒芙蕾与秋刀鱼"
    # 字符串
    print('msg is                               : ' + msg)
    # unicode编码
    print('transfer unicode msg to utf-8        : ' + msg.decode('utf-8').encode('gb2312'))
    # 居中
    print('center in 80                         : ' + msg.center(80, '='))
    # 首字母大写
    print('first upper                          : ' + msg.capitalize())
    # 查询子字符串数量
    print('count of n after str handle          : ' + str(msg.count('n', 10, msg.__len__())))
    # unicode解码
    print('transfer gb2312 msg to unicode       : ' + msg.decode('utf-8'), isinstance(msg.decode('utf-8'), unicode))
    # 是否以字符串结束
    print('endswith a str                       : ' + str(msg.endswith('舒芙蕾与秋刀鱼', -9, msg.__len__())))
    # 将\t转化为空格
    print('=====I\'m getting \tLonger...'.expandtabs(40))
    # 查询字符串开头索引
    print('find a str in msg                    : ' + str(msg.find('舒芙蕾与秋刀鱼')))
    print('find a str not in msg                : ' + str(msg.find('鱼籽酱')))
    # 格式化字符串
    name = "My name is {name} and i am {year} old"
    print('format str                           : ' + name.format(name='Sapphire', year=24))
    # 查询字符串位置
    print('index a str in msg                   : ' + str(msg.index('舒芙蕾与秋刀鱼')))
    # 是否为数字或字母
    print('is letters or nums                   : ' + str("12ab".isalnum()))
    # 是否为字母
    print('is alpha                             : ' + str("abc".isalpha()))
    # 是否为整数
    print('is digit                             : ' + str("123".isdigit()))
    # 是否为小写字母
    print('is lower                             : ' + str("abc".islower()))
    # 是否为大写字母
    print('is upper                             : ' + str("ABC".isupper()))
    # 是否为十进制
    # print('is decimal                           : ' + str("Ox11".isdecimal()))
    # 判断是不是一个合法的表示符(变量名)
    # print('is identifier                        : ' + str("_1_a".isidentifier()))
    # 是否只有数字
    # print('is numeric                           : ' + str("O123".isnumeric()))
    # 是否为空白
    print('is space                             : ' + str("     ".isspace()))
    # 是否每个首字母大写
    print('is all letters capitalized           : ' + str("My Boy".istitle()))
    # 拼接字符串
    print('join str                             : ' + ",".join("ABC"))
    # 长50不够用*号补上
    print('msg add right * to 80                : ' + msg.ljust(80, '*'))
    print('msg add left * to 80                 : ' + msg.rjust(80, '*'))
    # 转化字母
    print('lower str                            : ' + "Abc".lower())
    print('upper str                            : ' + "Abc".upper())
    # 从左边去掉空格回车
    print('delete the left space                : ' + "     A b c     ".lstrip())
    # 从右边去掉空格回车
    print('delete the right space               : ' + "     A b c     ".rstrip())
    # 去掉两边空格回车
    print('delete spaces on both sides          : ' + "     A b c     ".strip())

    # print(msg.translate(str.maketrans("abcde", "12345"), "舒芙蕾与秋刀鱼"))

    # 字符串替换
    print('replace msg                          : ' + msg.replace('舒芙蕾与秋刀鱼', '充电器和秋裤', 1))
    # 从右侧查找
    print('right find msg                       : ' + str(msg.rfind('秋')))
    # 分割成列表
    print('split msg                            : ' + str(msg.split('n')))
    # 匹配换行符，分割成列表
    print('splitlines msg                       : ' + str('1+2\n+3+4'.splitlines()))
    # 反转大小写
    print('swapcase msg                         : ' + 'SapphiRE'.swapcase())
    # 变成一个title
    print('title msg                            : ' + 'my boy'.title())
    # 不够50位就前面补零
    print('zfill 100                            : ' + '100'.zfill(50))
    # 从左查询，分割字符串
    print('partition n                          : ' + str('100'.partition("n")))
    # 从右查询，分割字符串
    print('rpartition n                         : ' + str('100'.rpartition("n")))
    print('doc of                               : ' + msg.__doc__)
    print('add Str                              : ' + msg.__add__(" Machine Learning"))
    print('class of                             : ' + str(msg.__class__))
    print('contains str                         : ' + str(msg.__contains__('舒芙蕾与秋刀鱼')))
    print('len of                               : ' + str(msg.__len__()))
    print('size of                              : ' + str(msg.__sizeof__()))
    print('str at 3                             : ' + msg[3])

print('''
===================================================================================================
=                                               Open                                              =
===================================================================================================
''')

print(__doc__)

print('''
===================================================================================================
=                                         Escape Character                                        =
===================================================================================================
''')

# 转义字符
print(escape_character.__doc__)
escape_character()

print('''
===================================================================================================
=                                         String Operator                                         =
===================================================================================================
''')

# 字符串运算符
print(string_operator.__doc__)
string_operator("Hello", 'Python')

print('''
===================================================================================================
=                                          String Format                                          =
===================================================================================================
''')

# 字符串格式化
print(string_format.__doc__)
string_format()

print('''
===================================================================================================
=                                         String Built-In                                         =
===================================================================================================
''')

# 字符串内建函数
print(string_build_in_function.__doc__)
string_build_in_function()

print('''
===================================================================================================
=                                             Closed                                              =
===================================================================================================
''')
