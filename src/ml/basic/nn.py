#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib
import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
matplotlib.use('TkAgg')
import matplotlib.pyplot as pyplot
import gzip
import shutil

class NeuralNet(object):
    def __init__(self, sizes):
        self.sizes = sizes
        self.num_layers = len(sizes)
        self.w = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.b = [np.random.randn(y, 1) for y in sizes[1:]]

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def sigmoid_prime(self, z):
        sigmoid = self.sigmoid(z)
        return sigmoid * (1 - sigmoid)

    def farward(self, x):
        for b, w in zip(self.b, self.w):
            x = self.sigmoid(np.dot(w, x) + b)
        return x

    # epoches: training times, eta: learning rate
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)

        n = len(training_data)
        print(epochs)
        for i in range(epochs):
            random.shuffle(training_data)
            mini_batchs = [training_data[k: k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for ind, mini_batch in enumerate(mini_batchs):
                print("batch {}".format(ind))
                self.update_mini_batch(mini_batch, eta)
                if test_data:
                     print("Epoch {0}: {1} / {2}".format(i, self.evaluate(test_data), n_test))
                else:
                    print("Epoch {0} complete".format(i))

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.b]
        nabla_w = [np.zeros(w.shape) for w in self.w]
        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.b, self.w):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) * self.sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.w[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.b]
        nabla_w = [np.zeros(w.shape) for w in self.w]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self_w = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.w, nabla_w)]
        self_b = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.b, nabla_b)]

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.farward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

    def predict(self, data):
        value = self.farward(data)
        return value.tolist().index(max(value))

    def save(self):
        pass

    def load(self):
        pass


def load_mnist(dataset="training_data", digits=np.arange(10), path="../mnist"):

    if dataset == "training_data":
        fname_image = os.path.join(path, 'train-images-idx3-ubyte.gz')
        fname_label = os.path.join(path, 'train-labels-idx1-ubyte.gz')
    elif dataset == "testing_data":
        fname_image = os.path.join(path, 't10k-images-idx3-ubyte.gz')
        fname_label = os.path.join(path, 't10k-labels-idx1-ubyte.gz')
    else:
        raise ValueError("dataset must be 'training_data' or 'testing_data'")

    # flbl = open(fname_label, 'rb')
    flbl = gzip.open(fname_label, 'rb')
    # magic_nr, size = struct.unpack(">II", flbl.read(8))
    magic_nr, size = struct.unpack(">2I", flbl.read(8))
    lbl = pyarray("b", flbl.read())
    # print(magic_nr, size)
    flbl.close()

    # fimg = open(fname_image, 'rb')
    fimg = gzip.open(fname_image, 'rb')
    # print(fimg.tell()) # refer to https://docs.python.org/2/tutorial/inputosizeutput.html
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    # magic_nr, size, rows, cols = struct.unpack(">4I", fimg.read(16))
    # print(magic_nr, size, rows, cols)
    img = pyarray("B", fimg.read())
    fimg.close()

    ind = [ k for k in range(size) if lbl[k] in digits ]
    N = len(ind)
    # print(N)

    images = zeros((N, rows, cols), dtype=uint8)
    labels = zeros((N, 1), dtype=int8)
    for i in range(N):
        images[i] = array(img[ ind[i] * rows * cols : (ind[i] + 1) * rows * cols ]).reshape((rows, cols))
        labels[i] = lbl[ind[i]]

    return images, labels

def load_samples(dataset="training_data"):

    image,label = load_mnist(dataset)

    X = [np.reshape(x, (28 * 28, 1)) for x in image]
    X = [x / 255.0 for x in X]
    # print(np.array(X).shape)

    # 5 -> [0,0,0,0,0,1.0,0,0,0];  1 -> [0,1.0,0,0,0,0,0,0,0]
    def vectorized_Y(y):
        e = np.zeros((10, 1))
        e[y] = 1.0
        return e

    if dataset == "training_data":
        Y = [vectorized_Y(y) for y in label]
        pair = list(zip(X, Y))
        return pair
    elif dataset == 'testing_data':
        pair = list(zip(X, label))
        # print(pair[:1], len(pair[1]))
        return pair
    else:
        print('Something wrong')


if __name__ == "__main__":
    net=NeuralNet([3,4,2])
    # print('weight: ',net.w)
    # print('biases: ',net.b)

    # x  = np.linspace(-8.0,8.0, 2000)
    # y = net.sigmoid(x)
    # pyplot.plot(x,y)
    # # pyplot.show()

    # array = np.arange(12)
    # random.shuffle(array)
    # array = array.reshape(3, 4)
    # print(array, np.argmax(array)) # max index
    # print("\nIndices of Max element : ", np.argmax(array, axis=0))
    # print("\nIndices of Max element : ", np.argmax(array, axis=1))

    # data = ""
    # with gzip.open('../mnist/t10k-labels-idx1-ubyte.gz', 'rb') as f_in:
    #     data = f_in.read()
    # # print(data)
    # print(np.zeros(3))
    # for item in array:
    #     print(item)

    # print(np.arange(10))
    # print(np.zeros((10, 1))) # 10 rows 1 col

    INPUT = 28*28
    OUTPUT = 10
    net = NeuralNet([INPUT, 40, OUTPUT])

    train_set = load_samples(dataset='training_data')
    test_set = load_samples(dataset='testing_data')

    net.SGD(train_set, 13, 10000, 3.0, test_data=test_set)

    correct = 0;
    for test_feature in test_set:
        if net.predict(test_feature[0]) == test_feature[1][0]:
            correct += 1
    print("accuracy: ", correct/len(test_set))
