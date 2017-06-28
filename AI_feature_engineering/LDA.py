# -*- coding: utf8 -*-
from sklearn.lda import LDA
def Lda( data,label ):
    str = raw_input("选择降维的维数:[1-%d]" % data.shape[1])
    n = int(str)
    print("从%d个特征中抽象出%d个特征" % (data.shape[1], n))
    lda = LDA(n_components=n)
    lda.fit(data,label)
    data_new = lda.transform(data)
    return data_new