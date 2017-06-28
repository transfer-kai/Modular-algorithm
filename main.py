# -*- coding: utf8 -*-
import AI_readdata.AI_readdata_csv as readdata
import AI_preprocessing.AI_fill_missing_value as fillmissingvalue
import AI_preprocessing.AI_standardization as standardization
import AI_preprocessing.AI_normalization as normalization
import AI_preprocessing.AI_type_transfer as featuretransform
import AI_preprocessing.AI_spilitdata as spilitdata
import AI_feature_engineering.PCA as PCA
import AI_feature_engineering.LDA as LDA
from AI_classification import KNN_Classifier,LR_Classifier,\
    NB_Classifier,SVM_Classifier,TREE_Classifier
from AI_preprocessing.AI_data_transfer import data_transfer
from AI_preprocessing.AI_label_encoder import labelencoder
import AI_evaluation.AI_evaluation_index as evaluation
import AI_evaluation.AI_evaluation_all as plot_all

import AI_writedata.AI_write2csv as writedata


if __name__ == '__main__':
    data, label = readdata.ReadData('./dataset/binary/credit_a.csv')
    label = labelencoder(label)
    data = data_transfer(data ,label)
    str_pre = raw_input("选择数据预处理方式：[ ST / NM ]")  # 标准化 & 归一化
    if str_pre == 'ST':
        data = normalization.Normalization(data)
    elif str_pre == 'NM':
        data = standardization.Standardization(data)
    str_ext = raw_input("选择特征降维方式: [ PCA / LDA ]")
    if str_ext == 'PCA':
        data = PCA.Pca(data)
    elif str_ext == 'LDA':
        data = LDA.Lda(data,label)
    trainx, testx, trainy, testy = spilitdata.split_data(data,label)
    str = raw_input("选择分类模型：[ KNN / NB / LR / TREE / SVM ]\n")
    if str == 'KNN':
        clf = KNN_Classifier.KNN()
    elif str == 'NB':
        clf = NB_Classifier.Gaussian_NB()
    elif str == 'LR':
        clf = LR_Classifier.LR()
    elif str == 'TREE':
        clf = TREE_Classifier.TREE()
    else:
        clf = SVM_Classifier.SVM()
    evaluation.evaluation(clf,trainx,trainy,testx,testy)
    plot_all.evaluation(trainx,trainy,testx,testy)
    # writedata.Writedata(clf.support_vectors_ ,'CLASSIFIER WEIGHTS')










