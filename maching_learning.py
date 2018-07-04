#author_by zhuxiaoliang
#2018-07-04 下午12:20

""""""

'''
bagging 和boosting 区别
集成学习：将已有的分类或者回归算法通过一定方式组合起来，形成一个性能更加强大的学习器。
        分为两类：个体学习器之间存在强依赖关系，必须串行化生成序列代表：boosting
                个体学习器之间不存在强依赖关系，可同时生成的并行化方法。代表是bagging和随机森林。
1、Bagging 并行化
  需要用到bootstraping，有放回的抽样方式。
  A、从原始样本中抽取训练集。进行k轮抽取，共生成k个训练集。每轮从原始样本中进行bootstaping方式进行抽取（即有的样本会被重复抽取，有的可能一次都没有抽到）
  B、每次使用一个训练集得到一个模型，共得到开个模型，随机森林使用的决策树算法。
  C、对于分类问题，k个模型得到的结果进行投票，回归问题：使用均值作为最终结果。
  一句话：k个训练集——>k个模型->结果：投票或者均值
2、boosting 将弱分类器组装成强分类器。
    串行化训练，减小前一轮被弱分类器分错样例的权值
    加法方式将弱分类器进行线性组合。
    例如AdaBoost给每个弱分类器一个权值，将其线性组合最为最终分类器。误差越小的弱分类器，权值越大
    使得在后面的分类器中得到关注。）
    
下面是将决策树与这些算法框架进行结合所得到的新的算法：

1）Bagging + 决策树 = 随机森林

2）AdaBoost + 决策树 = 提升树
之适用于二分类，给所有的弱分类器进行线性加权。

3）Gradient Boosting + 决策树 = GBDT

  
    
    
    
    
    
    
    
    
    
    
    
'''

"""
一、决策树


"""