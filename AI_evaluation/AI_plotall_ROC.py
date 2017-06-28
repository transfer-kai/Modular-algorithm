from matplotlib.pylab import plt
from sklearn.metrics import precision_recall_curve, roc_curve

def Plot_ROC(probas_,testy,clflist):
    i=0
    for prob in probas_:
        fpr, tpr, thresholds = roc_curve(testy, prob[:, 1])
        plt.plot(fpr,tpr , lw=1,label=clflist[i])
        i+=1
    plt.legend(loc='upper center', bbox_to_anchor=(0.65,0.2),ncol=3,fancybox=False,shadow=False)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC_picture')
    plt.show()