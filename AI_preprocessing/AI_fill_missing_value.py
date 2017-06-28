# -*- coding: utf8 -*-
from sklearn.preprocessing import Imputer

def missing_value(data):
    quest = raw_input("是否填充特征缺失值：[Y / N ]")
    if quest == 'Y':
        str = raw_input("替换为各列的：[ mean / median / most_frequent ]")
        imp = Imputer(missing_values='NaN',strategy=str ,axis=0)
        imp.fit(data)
        data = imp.transform(data)
    return data