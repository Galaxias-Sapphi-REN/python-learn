#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
ID3就是要从表的训练集构造图这样的决策树。实际上，能正确分类训练集的决策树不止一棵。Quinlan的ID3算法能得出结点最少的决策树。
ID3算法：
     ⒈ 对当前例子集合，计算各属性的信息增益（information gain）；
     ⒉ 选择信息增益最大的属性Ak；
     ⒊ 把在Ak处取值相同的例子归于同一子集，Ak取几个值就得几个子集；
     ⒋ 对既含正例又含反例的子集，递归调用建树算法；
     ⒌ 若子集仅含正例或反例，对应分枝标上P或N，返回调用处。
"""

from math import log

import operator


# 计算香农熵
def cal_shannon_entropy(dataSet):
    """
    1. traversal all the data in dataSet and build resultDict
            resultDict {
                key     :   last element of vec in dataSet
                value   :   count of last element
            }
    3. shannon entropy
            I = -∑plog2(p)
    :param dataSet:
    :return:Statistical quantity

    """
    # build resultDict
    resultDict = {}
    lastFeat = [data[-1] for data in dataSet]
    uniqueVals = set(lastFeat)
    for value in uniqueVals:
        resultDict[value] = lastFeat.count(value)

    # cal shannonEnt I = -∑plog2(p)
    totalNum = len(dataSet)
    shannonEnt = 0.0
    for key in resultDict:
        prob = float(resultDict[key]) / totalNum
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按照给定的特征划分数据集
def split_data(dataSet, axis, value):
    """
    _dataSet = [
        [1, 'a', 'c', 4],
        [2, 'a', 'c', 3],
        [1, 'b', 'c', 4],
        [2, 'a', 'd', 3]
    ]
    print(split_data(_dataSet, 1, 'a'))

    [[1, 'c', 4], [2, 'c', 3], [2, 'd', 3]]

    :param dataSet:
    :param axis:
    :param value:
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:  # abstract the fature
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择信息增益最大的属性
def choose_best_feature_to_split(dataSet):
    """
    1. 遍历各个子集并且计算该子集的熵
    2. 该分支（子集）伤的编码信息
        Gain(A) = I(A) - E(A)
            其中
            I(A)是香农熵
            E(A)是子集熵
                E(A) = 各个子集香农熵的权和 ∑(s/S)I(A)
    3. 比较返回最高的编码信息

    分枝将获得的编码信息是                                                。
    :param dataSet:
    :return:
    """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = cal_shannon_entropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 遍历数据集中每一条数据相同的特性集合
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            # 为数据集合dataSet第i列的value特征划分数据集
            subDataSet = split_data(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * cal_shannon_entropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# 递归创建树，用于找出出现次数最多的分类名称的函数
def majority_cnt(classList):
    classCount = {}
    for vote in classList:
        if vote in classCount.keys():
            classCount[vote] = 1
        else:
            classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 创建树
def create_tree(dataSet, labels):
    # 取数据集最后一项为结果集
    classList = [example[-1] for example in dataSet]
    # 结果集所有结果都为第一项的值，则停止匹配
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # traversal all the features and choose the most frequent feature
    if len(dataSet[0]) == 1:
        return majority_cnt(classList)
    bestFeat = choose_best_feature_to_split(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # get the list which attain the whole properties
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = create_tree(split_data(dataSet, bestFeat, value), subLabels)
    return myTree


# 打印决策树
def print_tree(decisionTree, deep=0):
    """
    {
        '喝水':
        {
            '>7杯': '水桶'
            '<7杯': '水货'
        }
    }
    :param decisionTree:    决策树
    :param deep:            深度
    :return:
    """
    for key in decisionTree:
        if type(decisionTree[key]) is dict:
            print('\t' * (deep + 1) + ' -> ' + str(key) + " : ")
            deep += 1
            print_tree(decisionTree[key], deep)
        else:
            print('\t' * (deep + 1) + ' -> ' + str(key) + " : " + str(decisionTree[key]))


# 决策树分类匹配
def classify(decisionTree, features, testVec):
    if len(testVec) != len(features) - 1:
        print("输入的测试数据不匹配！数据长度应为：" + str(len(features) - 1))
        return
    firstFeat = decisionTree.keys()[0]
    nextDecisionTree = decisionTree[firstFeat]
    featIndex = features.index(firstFeat)
    if featIndex > len(testVec) - 1:
        print("决策树中不存在该信息！" + firstFeat)
        return
    classLabel = None
    hasFind = False
    for key in nextDecisionTree.keys():
        if str(testVec[featIndex]) == key:
            hasFind = True
            if type(nextDecisionTree[key]).__name__ == 'dict':
                classLabel = classify(nextDecisionTree[key], features, testVec)
            else:
                classLabel = nextDecisionTree[key]
    if classLabel is None and not hasFind:
        print("该样本特性未经过训练：" + str(testVec[featIndex]) + "（" + firstFeat + "）")
    return classLabel
