# -*- coding: utf8 -*-
from sklearn.decomposition import PCA
def Pca(data):
    str2 = raw_input("选择降维的维数:[1-%d]" % data.shape[1])
    n = int(str2)
    print("从%d个特征中抽象出%d个特征" % (data.shape[1], n))
    pca = PCA(n_components= n ,whiten=True)
    pca.fit(data)
    data_new = pca.transform(data)
    return data_new