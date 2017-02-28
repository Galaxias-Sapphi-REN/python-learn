#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
1 : the patient should be fitted with hard contact lenses,
2 : the patient should be fitted with soft contact lenses,
3 : the patient should not be fitted with contact lenses.

1. age of the patient: (1) young, (2) pre-presbyopic, (3) presbyopic
2. spectacle prescription: (1) myope, (2) hypermetrope
3. astigmatic: (1) no, (2) yes
4. tear production rate: (1) reduced, (2) normal
"""
from id3 import *


# 获取数据源
def get_data_set():
    """ AllElectronics顾客数据库元组训练集 数据来源：http://archive.ics.uci.edu/ml/datasets/Lenses """
    fp = open("lenses.data")
    str_data_set = fp.readlines()
    data_set = [line.split()[1:] for line in str_data_set]
    labels = ['年龄类型', '远近视表现', '散光类型', '泪液分泌率类型', '配镜类型']
    return data_set, labels


# 打印糖
def printResult(decisionTree, features, featVec):
    num = len(featVec)
    welcome = '病人来惹!\n乔巴-诊断：'
    for i in range(num):
        welcome += str(features[i]) + ' : ' + str(featVec[i]) + '; '
    print(welcome)
    result = classify(decisionTree, features, featVec)
    if result == '1':
        print('the patient should be fitted with hard contact lenses!')
    elif result == '2':
        print('the patient should be fitted with soft contact lenses!')
    elif result == '3':
        print('the patient should not be fitted with contact lenses!')
    else:
        print('no lenses!')


myDate, myLabels = get_data_set()
myTree = create_tree(myDate, myLabels)
print_tree(myTree)

print(__doc__)
myDate, myLabels = get_data_set()
printResult(myTree, myLabels, [3, 1, 1, 1])
printResult(myTree, myLabels, [1, 1, 1, 2])
printResult(myTree, myLabels, [1, 1, 1, 4])
