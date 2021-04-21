"""
Machine learning TPH via TensorFlow RNN.

TensorFlow is "An end-to-end open source machine learning platform."
Please visit https://www.tensorflow.org
TPH is temperature, pressure and humidity.
RNN is Recurrent Neural Network.

Keras
is a high-level API that's easier for ML beginners, as well as researchers.
Keras overview
https://www.tensorflow.org/guide/keras/overview
Recurrent Neural Network with Keras.
https://www.tensorflow.org/guide/keras/rnn

@date 12 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""
# from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import collections
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from tensorflow.keras import layers
logger = logging.getLogger(__name__)


def buildSequentialModel(id=1000, od=64, ll=128, dl=10):
    """
    Build a simple model.

    See:
        https://www.tensorflow.org/guide/keras/rnn#build_a_simple_model

    Params:
        id (int): (input_dim) Embedding layer expecting input vocab of size
        od (int): (output_dim) output embedding dimension of size
        ll (int): (lstm_layer) LSTM layer internal units
        dl (int): (dense_layer) Dense layer units

    Returns:
        model: tensorflow.keras.Sequential
    """
    logger.debug(f'start, id: {id}, od: {od}, ll: {ll}, dl: {dl}')

    model = tf.keras.Sequential()
    model.add(layers.Embedding(input_dim=id, output_dim=od))
    model.add(layers.LSTM(ll))
    model.add(layers.Dense(dl))
    logger.debug(f'model.summary: {model.summary()}')

    logger.debug('end')
    return model
