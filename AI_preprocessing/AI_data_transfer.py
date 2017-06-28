import numpy as np
from numpy import *
from sklearn import preprocessing
def data_transfer(data,label):
    le = preprocessing.LabelEncoder()
    data_new = np.array(list())
    length = len(data[0])  # number of feaures
    length_y = len(label) # number of samples
    for i in range(length):
        if isinstance(data[0][i], str): # if i-th feature is string
            str_data = data[:, i]
            le.fit(str_data)
            str_labelencoder = le.transform(str_data)
        else:
            str_labelencoder = data[:, i]
        str_labelencoder = str_labelencoder.reshape((length_y, -1))
        if i == 0:
            data_new = str_labelencoder
        else:
            data_new = np.concatenate([data_new, str_labelencoder], axis=1)
    data = data_new.astype(dtype='float')
    return data