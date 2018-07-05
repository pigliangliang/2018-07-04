#author_by zhuxiaoliang
#2018-07-04 下午4:46

import numpy as np

def loadDataSet():
    postingList = [
        ['my','dog','has','flea','help','please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid'],
    ]
    classVec = [0,1,0,1,0,1]#1代表不好，0代表中性
    return  postingList,classVec

#创建一个在文档中出现的不重复词的列表，字典
def createVocabList(dataSet):
    vocabset = set()
    for document in dataSet:
        vocabset = vocabset|set(document)
    return list(vocabset)


alllist,alllable = loadDataSet()
vobcab = createVocabList(alllist)
print(vobcab)
'''['quit', 'worthless', 'has', 'stop', 'love', 'buying', 'is', 'ate', 'licks', 'mr', 'to', 'steak', 'I', 'flea', 'dalmation', 'food', 'cute', 'stupid', 'how', 'not', 'so', 'help', 'garbage', 'my', 'please', 'dog', 'posting', 'park', 'him', 'maybe', 'take']
'''

#将单词装换为词向量 ,one-hot 编码

def setofWords2Vec(vocabList,inputSet):
    retVec = [0]*len(vocabList)

    for word in inputSet:
        if word in vocabList:
            retVec[vocabList.index(word)] +=1
    return retVec

trainmat = []
for a in alllist:

     trainmat.append(setofWords2Vec(vobcab,a))
print(trainmat)
"""
[[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]

"""
def testNB0(trainMatrix,trainlable):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive= sum(trainlable)/float(numWords)
    p0num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainlable[i] ==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0num +=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])

    p1Vect = np.log(p1Num/p1Denom)
    p0Vect = np.log(p0num/p0Denom)
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify*p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify*p0Vec) + np.log(1.0-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

