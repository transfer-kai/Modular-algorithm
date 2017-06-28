# -*- coding: utf8 -*-
from AI_plotall_ROC import Plot_ROC
from AI_classification import KNN_Classifier,LR_Classifier,\
    NB_Classifier,SVM_Classifier,TREE_Classifier

def evaluation(trainx,trainy,testx,testy):
    clfs = []
    probas_ = []
    clfs.append(KNN_Classifier.KNN())
    clfs.append(NB_Classifier.Gaussian_NB())
    clfs.append(LR_Classifier.LR())
    clfs.append(TREE_Classifier.TREE())
    clfs.append(SVM_Classifier.SVM())
    clflist =['KNN','NB','LR','TREE','SVM']
    for clf in clfs:
        clf.fit(trainx, trainy)
        probas_.append(clf.predict_proba(testx))
    Plot_ROC(probas_,testy,clflist)


