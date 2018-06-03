#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn import svm
import numpy as np
import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
import pickle

def load_samples(dataset="training_data"):
    image,label = load_mnist(dataset)

    X = [np.reshape(x,(28*28)) for x in image]
    X = [x/255.0 for x in X]
    #print(X.shape)

    pair = list(zip(X, label))
    return pair

if __name__ == '__main__':

    train_set = load_samples(dataset='training_data')
    test_set = load_samples(dataset='testing_data')

    train_X = []
    train_Y = []
    for feature in train_set:
        train_X.append(feature[0])
        train_Y.append(feature[1][0])

    clf = svm.SVR()
    clf.fit(train_X, train_Y)

    #with open('minst.module', 'wb') as f:
    #pickle.dump(clf, f)

    #with open('minst.module', 'rb') as f:
    #   clf = pickle.load(f)

    test_X = []
    test_Y = []
    for feature in test_set:
        test_X.append(feature[0])
        test_Y.append(feature[1][0])

    correct = 0
    i = 0
    for feature in test_X:
        predict = clf.predict(np.array(feature).reshape(1, -1))
        if round(float(predict)) == test_Y[i]:
            correct += 1
        i = i + 1
    print("accuracy: ", correct/len(test_X))