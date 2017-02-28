#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on 2017-1-24

@author: sapphire

量化分析的工作涉及到大量的数值运算，一个高效方便的科学计算工具是必不可少的。
Python语言一开始并不是设计为科学计算使用的语言，随着越来越多的人发现Python的易用性，逐渐出现了关于Python的大量外部扩展，
NumPy (Numeric Python)就是其中之一。NumPy提供了大量的数值编程工具，可以方便地处理向量、矩阵等运算，
极大地便利了人们在科学计算方面的工作。另一方面，Python是免费，相比于花费高额的费用使用Matlab，
NumPy的出现使Python得到了更多人的青睐。

http://scipy.github.io/old-wiki/pages/Numpy_Example_List
https://docs.scipy.org/doc/numpy/
"""
import numpy as np

print(np.version.full_version)

print("构造一维数组")
# 初窥NumPy对象：数组。NumPy中的基本对象是同类型的多维数组（homogeneous multidimensional array）
a = np.arange(20)
print(a)
print(type(a))

print("构造二维数组")
# 通过函数"reshape"，我们可以重新构造一下这个数组，例如，我们可以构造一个4*5的二维数组
# 其中"reshape"的参数表示各维度的大小，且按各维顺序排列（两维时就是按行排列，这和R中按列是不同的）
a = a.reshape(4, 5)
print(a)

print("构造三维数组")
a = a.reshape(2, 2, 5)
print(a)

# "ndim"查看维度；
# "shape"查看各维度的大小；
# "size"查看全部的元素个数，等于各维度大小的乘积；
# "dtype"可查看元素类型；
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# 创建数组
print("创建数组")
raw = [0, 1, 2, 3, 4]
a = np.array(raw)
print(a)
raw = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
b = np.array(raw)
print(b)
# 一些特殊的数组有特别定制的命令生成，如4*5的全零矩阵：
d = (4, 5)
print(np.zeros(d))
# 默认生成的类型是浮点型，可以通过指定类型改为整型：
print(np.ones(d, dtype=int))
# [0, 1)区间的随机数数组：
print(np.random.rand(5))

# 数组操作
# 数组内元素是同质的
print("数组操作")
a = np.array([[1.0, 2], [2, 4]])
print("a                        : \n" + str(a))
b = np.array([[3.2, 1.5], [2.5, 4]])
print("b                        : \n" + str(b))
print("a + b                    : \n" + str(a + b))
print("3 * a                    : \n" + str(3 * a))
print("1.8 + a                  : \n" + str(1.8 + a))
print("a/2                      : \n" + str(a / 2))
print("np.exp(a)                : \n" + str(np.exp(a)))
print("np.sqrt(a)               : \n" + str(np.sqrt(a)))
print("np.square(a)             : \n" + str(np.square(a)))
print("np.power(a,3)            : \n" + str(np.power(a, 3)))

a = np.arange(20).reshape(4, 5)
print("a                        : \n" + str(a))
print("sum                      : " + str(a.sum()))
print("maximum                  : " + str(a.max()))
print("minimum                  : " + str(a.min()))
print("maximum in each row      : " + str(a.max(axis=1)))
print("minimum in each column   : " + str(a.min(axis=0)))

# 科学计算中大量使用到矩阵运算，除了数组，NumPy同时提供了矩阵对象（matrix）。
# 矩阵对象和数组的主要有两点差别：
# 一是矩阵是二维的，而数组的可以是任意正整数维；
# 二是矩阵的'*'操作符进行的是矩阵乘法，乘号左侧的矩阵列和乘号右侧的矩阵行要相等，而在数组中'*'操作符进行的是每一元素的对应相乘，乘号两侧的数组每一维大小需要一致。
# 数组可以通过asmatrix或者mat转换为矩阵，或者直接生成也可以：
a = np.arange(20).reshape(4, 5)
a = np.asmatrix(a)
print(a)
print(type(a))

b = np.matrix('1.0 2.0; 3.0 4.0')
print(b)
print(type(b))

# 再来看一下矩阵的乘法，这使用arange生成另一个矩阵b，
# arange函数还可以通过arange(起始，终止，步长)的方式调用生成等差数列，注意含头不含尾。
b = np.arange(2, 45, 3).reshape(5, 3)
b = np.mat(b)
print(b)

# arange指定的是步长，如果想指定生成的一维数组的长度怎么办？好办，"linspace"就可以做到：
print(np.linspace(0, 2, 9))
print("a                        : \n" + str(a))
print("b                        : \n" + str(b))
print("a * b                    : \n" + str(a * b))

a = np.mat(np.arange(6).reshape(2, 3))
b = np.mat(np.arange(6).reshape(3, 2))
print("a                        : \n" + str(a))
print("b                        : \n" + str(b))
print("a * b                    : \n" + str(a * b))

# 数组元素访问
a = np.array([[3.2, 1.5], [2.5, 4]])
b = a
a[0][1] = 2.0
print("a                        : \n" + str(a))
print("b                        : \n" + str(b))
a = np.array([[3.2, 1.5], [2.5, 4]])
b = a.copy()
a[0][1] = 2.0
print("a                        : \n" + str(a))
print("b                        : \n" + str(b))
# 利用':'可以访问到某一维的全部数据，例如取矩阵中的指定列：
a = np.arange(20).reshape(4, 5)
print("a                        : \n" + str(a))
print("the 1st and 2nd column   : \n" + str(a[:, [0, 1]]))
# 稍微复杂一些，我们尝试取出满足某些条件的元素，这在数据的处理中十分常见，通常用在单行单列上。下面这个例子是将第一列大于5的元素（10和15）对应的第三列元素（12和17）取出来：
print("...                      : \n" + str(a[:, 2][a[:, 0] > 5]))
# 可使用where函数查找特定值在数组中的位置：
loc = np.where(a == 11)
print(loc)
print(a[loc[0][0], loc[1][0]])

# 数组操作
# 首先来看矩阵转置：
a = np.random.rand(2, 4)
print("a                        : \n" + str(a))
a = np.transpose(a)
print("a is an array, by using transpose(a):")
print(a)
b = np.random.rand(2, 4)
b = np.mat(b)
print("b                        : \n" + str(b))
print("b is a matrix, by using b.T:")
print(b.T)
# 矩阵求逆：
# TODO 与期望结果不一致
a = np.mat(np.random.rand(2, 2))
print("a                        : \n" + str(a))
ia = np.linalg.inv(a)
print("inverse of a             : \n" + str(ia))
print("a * inv(a)               : \n" + str(a * ia))
# 求特征值和特征向量
# TODO 与期望结果不一致
a = np.random.rand(3, 3)
eig_value, eig_vector = np.linalg.eig(a)
print("eigen value              : \n" + str(eig_value))
print("eigen vector             : \n" + str(eig_vector))
# 按列拼接两个向量成一个矩阵：
a = np.array((1, 2, 3))
b = np.array((2, 3, 4))
print(np.column_stack((a, b)))
# 在循环处理某些数据得到结果后，将结果拼接成一个矩阵是十分有用的，可以通过vstack和hstack完成：
# TODO 与期望结果不一致
a = np.random.rand(2, 2)
b = np.random.rand(2, 2)
print("a                        : \n" + str(a))
print("b                        : \n" + str(b))
print("horizontal stacking a,b  : \n" + str(np.hstack([a, b])))
print("vertical stacking a,b    : \n" + str(np.vstack([a, b])))

# 缺失值
# 缺失值在分析中也是信息的一种，NumPy提供nan作为缺失值的记录，通过isnan判定。
a = np.random.rand(2, 2)
a[0, 1] = np.nan
print(np.isnan(a))
# nan_to_num可用来将nan替换成0，在后面会介绍到的更高级的模块pandas时，我们将看到pandas提供能指定nan替换值的函数。
print(np.nan_to_num(a))

