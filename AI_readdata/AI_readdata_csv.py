import numpy as np
import pandas as pd
from numpy import *
from pandas import Series,DataFrame
'''
def ReadData( path):
    csvfile = open(path, 'r')
    data = []
    label = []
    for line in csvfile:
        a = line.strip().split(',')
        data.append(a[:-1])
        label.append(a[-1])
    data = np.array(data).astype(dtype='float')
    label = np.array(label).astype(dtype='float')
    return data, label
'''
def ReadData(path):
    csvfile=pd.read_csv(path,header=None)
    csvfile=csvfile.fillna(method='ffill')
    csvdata=csvfile.values
    data=csvdata[:,0:-1]
    label=csvdata[:,-1]
    return data,label
