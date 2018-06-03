#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import datetime

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('/tmp/', one_hot=True)


n_input_layer = 28*28  # input

n_layer_1 = 500     # hide layer
n_layer_2 = 1000    # hide layer
n_layer_3 = 300     # hide layer

n_output_layer = 10   # output

def neural_network(data):
    layer_1_w_b = {'w_':tf.Variable(tf.random_normal([n_input_layer, n_layer_1])), 'b_':tf.Variable(tf.random_normal([n_layer_1]))}
    layer_2_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_1, n_layer_2])), 'b_':tf.Variable(tf.random_normal([n_layer_2]))}
    layer_3_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_2, n_layer_3])), 'b_':tf.Variable(tf.random_normal([n_layer_3]))}
    layer_output_w_b = {'w_':tf.Variable(tf.random_normal([n_layer_3, n_output_layer])), 'b_':tf.Variable(tf.random_normal([n_output_layer]))}

    # w·x+b
    layer_1 = tf.add(tf.matmul(data, layer_1_w_b['w_']), layer_1_w_b['b_'])
    layer_1 = tf.nn.relu(layer_1)
    layer_2 = tf.add(tf.matmul(layer_1, layer_2_w_b['w_']), layer_2_w_b['b_'])
    layer_2 = tf.nn.relu(layer_2 )
    layer_3 = tf.add(tf.matmul(layer_2, layer_3_w_b['w_']), layer_3_w_b['b_'])
    layer_3 = tf.nn.relu(layer_3 )
    layer_output = tf.add(tf.matmul(layer_3, layer_output_w_b['w_']), layer_output_w_b['b_'])

    return layer_output

batch_size = 100

X = tf.placeholder('float', [None, 28*28])
Y = tf.placeholder('float')

def train_neural_network(X, Y):
    predict = neural_network(X)
    cost_func = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict, labels=Y))
    optimizer = tf.train.AdamOptimizer().minimize(cost_func)  # learning rate default 0.001

    epochs = 13
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        epoch_loss = 0
        for epoch in range(epochs):
            for i in range( int(mnist.train.num_examples / batch_size) ):
                x, y = mnist.train.next_batch(batch_size)
                _, c = session.run([optimizer, cost_func], feed_dict={X:x, Y:y})
                epoch_loss += c
            print(epoch, ' : ', epoch_loss)

        # print(predict.eval(feed_dict={X:[features]}))
        correct = tf.equal(tf.argmax(predict,1), tf.argmax(Y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print('accuracy: ', accuracy.eval({X:mnist.test.images, Y:mnist.test.labels}))


if __name__ == '__main__':
    t1 = datetime.datetime.now()
    # with tf.device(assign_to_device('/cpu:0')):
    with tf.device('/cpu:0'):
      train_neural_network(X,Y)
    t2 = datetime.datetime.now()

    print(t2 - t1)

    # with tf.device(assign_to_device('/gpu:0', ps_device='/cpu:0')):
    # with tf.device(assign_to_device('/gpu:0')):
    # with tf.device('/gpu:0'):
    #   train_neural_network(X,Y)
    # t3 = datetime.datetime.now()

    # print(t3 - t2)

    # https://github.com/tensorflow/models/blob/master/official/mnist/mnist_tpu.py TPU example