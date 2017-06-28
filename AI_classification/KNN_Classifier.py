from sklearn.neighbors import KNeighborsClassifier

def KNN(n_neighbors=10):
    clf = KNeighborsClassifier(n_neighbors)
    return clf


