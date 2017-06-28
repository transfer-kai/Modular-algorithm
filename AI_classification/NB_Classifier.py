from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB


def Gaussian_NB():
        clf = GaussianNB()
        return clf


def Multinomial_NB():
        clf = MultinomialNB()
        return clf


def Bernoulli_NB():
        clf = BernoulliNB()
        return clf