from sklearn.cross_validation import train_test_split


def split_data(data, label):
    # train test split
    trainx, testx, trainy,testy = train_test_split(data, label, test_size=0.3)
    return trainx, testx, trainy, testy
  