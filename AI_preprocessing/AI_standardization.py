# -*- coding: utf8 -*-
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
# z - score standarization : x =(x_i - mean) / standard
# after z -score standarization ,x follows N(0,1)
# min-max Standarization : x = (x_i - min)/(max -min)
# after min -max standarization x will range from (0,1)

def Standardization(data):
    str = raw_input("选择标准化方法：[ Z / MINMAX / NO]")
    if str == 'Z':
        scaler = StandardScaler().fit(data)
        data_new = scaler.transform(data)
    elif str == 'MINMAX':
        min_max_scaler = MinMaxScaler()
        data_new = min_max_scaler.fit_transform(data)
    else:
        data_new =data
    return data_new


