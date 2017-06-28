# -*- coding: utf8 -*-
from sklearn import svm
#默认C=1.0;kernel='rbf',可选:linear,poly,rbf,sigmoid,precomputed
def SVM(c=1.0, kernel='rbf'):
        clf = svm.SVC(c, kernel, probability=True)
        return clf