#!/usr/bin/python
# encoding: utf-8
print('''
Created on 2017-1-18

@author: sapphire

【简介】
Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
Python 是交互式语言： 这意味着，您可以在一个Python提示符，直接互动执行写你的程序。
Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。


【历史】
Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。
Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。
像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。
现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。

Python的创始人为吉多·范罗苏姆（Guido van Rossum）。1989年的圣诞节期间，吉多·范罗苏姆为了在阿姆斯特丹打发时间，
决心开发一个新的脚本解释程序，作为ABC语言的一种继承。
注：ABC语言是由Guido参与设计的一种教学语言，是专门为非专业程序员设计的。就Guido本人看来，ABC这种语言非常优美和强大，
但是ABC语言并没有成功，究其原因，Guido认为是非开发造成的。Guido决心在Python中避免这一错误。
同时，他还想实现在ABC中闪现过但未曾实现的东西。（百度百科）

 Python可以应用于众多领域，如：数据分析、组件集成、网络服务、图像处理、数值计算和科学计算等众多领域。
 目前业内几乎所有大中型互联网企业都在使用Python，如：Youtube、Dropbox、BT、Quora（中国知乎）、豆瓣、知乎、Google、
 Yahoo！、facebook、NASA、百度、腾讯、汽车之家、美团等。
 互联网公司广泛使用Python来做的事一般有：自动化运维、自动化测试、大数据分析、爬虫、web等。


【特点】
1.易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。
2.易于阅读：Python代码定义的更清晰。
3.易于维护：Python的成功在于它的源代码是相当容易维护的。
4.一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。
5.互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。
6.可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。
7.可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。
8.数据库：Python提供所有主要的商业数据库的接口。
9.GUI编程：Python支持GUI可以创建和移植到许多系统调用。
10.可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。


【标识符】
在python里，标识符有字母、数字、下划线组成。
在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
python中的标识符是区分大小写的。
以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。


【保留字】
大小写敏感
and	        exec	    not
assert	    finally	    or
break	    for	        pass
class	    from	    print
continue	global	    raise
def	        if	        return
del	        import	    try
elif	    in	        while
else	    is	        with
except	    lambda	    yield


【严格缩进】
学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。
python最具特色的就是用缩进来写模块。
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

IndentationError: unexpected indent                                     tab和空格没对齐的问题
ndentationError: unindent does not match any outer indentation level    使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。


【多行语句】
total = item_one + \
        item_two + \
        item_three
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

【引号】
单引号( \' )
双引号( \" )
三引号( \'\'\'  \"\"\" )

【注释】
#
\'\'\'
\"\"\"
''')