#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
买电脑
"""
from id3 import *

# 获取数据源
def get_data_set():
    # AllElectronics顾客数据库元组训练集
    data_set = [
        ['<=30', '高', '否', '一般', '不会购买'],
        ['<=30', '高', '否', '良好', '不会购买'],
        ['>30 <=40', '高', '否', '一般', '会购买'],
        ['>40', '中', '否', '一般', '会购买'],
        ['>40', '低', '是', '一般', '会购买'],
        ['>40', '低', '是', '良好', '不会购买'],
        ['>30 <=40', '低', '是', '良好', '会购买'],
        ['<=30', '中', '否', '一般', '不会购买'],
        ['<=30', '低', '是', '一般', '会购买'],
        ['>40', '中', '是', '一般', '会购买'],
        ['<=30', '中', '是', '良好', '会购买'],
        ['>30 <=40', '中', '否', '良好', '会购买'],
        ['>30 <=40', '高', '是', '一般', '会购买'],
        ['>40', '中', '否', '良好', '不会购买'],
    ]
    labels = ['年龄', '收入', '学生', '信用信息', '是否购买']
    return data_set, labels


myDate, myLabels = get_data_set()
decisionTree = create_tree(myDate, myLabels)
print_tree(decisionTree)

myDate, myLabels = get_data_set()
print(classify(decisionTree, myLabels, ['>40', '中', '是', '良好']))
print(classify(decisionTree, myLabels, ['>40', '哦', '非常差']))
print(classify(decisionTree, myLabels, ['>40', '中', '哦', '非常差']))
print(classify(decisionTree, myLabels, ['<=30', '中', '否', '非常差']))
print(classify(decisionTree, myLabels, ['<=30', '中', '哦', '非常差']))
print(classify(decisionTree, myLabels, ['100', '中', '哦', '非常差']))
