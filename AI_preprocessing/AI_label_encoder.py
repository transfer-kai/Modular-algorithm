from sklearn import preprocessing

def labelencoder(label):
    le=preprocessing.LabelEncoder()
    le.fit(label)
    label_new=le.transform(label)
    return label_new