# -*- coding: utf8 -*-
from sklearn.preprocessing import normalize
# normalization : x_i /(sum(x_i))
# is the element /(sum of all the elements)
#  so that every value lies in (0,1) and their summation is 1

def Normalization(data):
         data_new = normalize(data)
         return data_new
