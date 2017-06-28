# -*- coding: utf8 -*-
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def Transform(data,label):
    data_new = data
    label_new = label
    str = raw_input("选择特征编码类型： [ binarization(特征二值化)/ label_binarization(标签二值化)\n/ label_encoding(标签编码)..."
                    "/onehot_encoder(类别型变数值型) /no_operation(保持原特征)]\n")
    if str =='binarization':
        thresh = float(raw_input("请选择特征的阈值："))
        binarizer = Binarizer(threshold=thresh)
        data_new = binarizer.transform(data)
    elif str == 'label_binarization':
        lb = LabelBinarizer() # neg_label =0 ,pos =1
        label_new = lb.transform(label)
    elif str == 'label_encoding':
        dic = {}
        for i in label:
            dic = dic.get(i,0) + 1
        le = LabelEncoder()
        le.fit(dic.keys())
        label_new = le.transform(label)
    elif str == 'onehot_encoder':
        enc = OneHotEncoder()
        enc.fit(data)
        data_new = enc.transform(data).toarray()
    elif str=='no_operation':
        data_new=data_new
        label_new=label_new
    return data_new,label_new


