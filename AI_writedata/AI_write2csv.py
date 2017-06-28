import csv
import numpy as np

def Writedata(Var,Name):
    with open(Name+'.csv','wb')as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        Var = np.array(Var)
        for i in range(Var.shape[0]):
            writer.writerow(Var[0])