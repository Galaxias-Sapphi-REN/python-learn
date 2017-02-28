#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
算法原理
决策树（Decision Tree）是一种简单但是广泛使用的分类器。通过训练数据构建决策树，可以高效的对未知的数据进行分类。
决策数有两大优点：
    1）决策树模型可以读性好，具有描述性，有助于人工分析；
    2）效率高，决策树只需要一次构建，反复使用，每一次预测的最大计算次数不超过决策树的深度。

基本步骤
决策树构建的基本步骤如下：
1. 开始，所有记录看作一个节点
2. 遍历每个变量的每一种分割方式，找到最好的分割点
3. 分割成两个节点N1和N2
4. 对N1和N2分别继续执行2-3步，直到每个节点足够“纯”为止
决策树的变量可以有两种：
1） 数字型（Numeric）：变量类型是整数或浮点数，如前面例子中的“年收入”。用“>=”，“>”,“<”或“<=”作为分割条件（排序后，利用已有的分割情况，可以优化分割算法的时间复杂度）。
2） 名称型（Nominal）：类似编程语言中的枚举类型，变量只能重有限的选项中选取，比如前面例子中的“婚姻情况”，只能是“单身”，“已婚”或“离婚”。使用“=”来分割。

如何评估分割点的好坏？如果一个分割点可以将当前的所有节点分为两类，使得每一类都很“纯”，也就是同一类的记录较多，那么就是一个好分割点。
比如上面的例子，“拥有房产”，可以将记录分成了两类，“是”的节点全部都可以偿还债务，非常“纯”；“否”的节点，
可以偿还贷款和无法偿还贷款的人都有，不是很“纯”，但是两个节点加起来的纯度之和与原始节点的纯度之差最大，所以按照这种方法分割。
构建决策树采用贪心算法，只考虑当前纯度差最大的情况作为分割点。
"""
from id3 import *


# 获取数据源
def get_data_set():
    """ 数据来源：http://www.cnblogs.com/bourneli/archive/2013/03/15/2961568.html """
    fp = open("repay.data")
    str_data_set = fp.readlines()
    labels = str_data_set[0][1:]
    str_data_set = str_data_set[1:]
    data_set = [line.split()[1:] for line in str_data_set]
    return data_set, labels


# 打印糖
def printResult(decisionTree, features, featVec):
    num = len(featVec)
    welcome = '客户来了!\n乔巴-诊断：'
    for i in range(num):
        welcome += str(features[i]) + ' : ' + str(featVec[i]) + '; '
    print(welcome)
    result = classify(decisionTree, features, featVec)
    print(result)


myDate, myLabels = get_data_set()
myTree = create_tree(myDate, myLabels)
print_tree(myTree)
print(__doc__)
myDate, myLabels = get_data_set()
printResult(myTree, myLabels, ['否','单身','55'])
printResult(myTree, myLabels, [1, 1, 1, 2])
printResult(myTree, myLabels, [1, 1, 1, 4])
