#!/usr/bin/env python3
"""
Load and sore sample datas for ML(Machine Learning).

I got datas from Japan Metrological Agency aka Kishou-chou.
https://www.data.jma.go.jp/gmd/risk/obsdl/index.php
https://www.jma.go.jp/jma/index.html

TensorFlow is "An end-to-end open source machine learning platform."
Please visit https://www.tensorflow.org
TPH is temperature, pressure and humidity.
RNN is Recurrent Neural Network.

Keras
is a high-level API that's easier for ML beginners, as well as researchers.
Keras overview
https://www.tensorflow.org/guide/keras/overview
`Recurrent Neural Networks (RNN) with Keras. <https://www.tensorflow.org/guide/keras/rnn>`_

Keras Documentation
https://keras.io

Weather forecasting with Recurrent Neural Networks in Python
https://medium.com/analytics-vidhya/weather-forecasting-with-recurrent-neural-networks-1eaa057d70c3

@date 1 April 2020
@author mitsuhisaT <asihustim@gmail.com>
"""
import os
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# pip install git+https://github.com/tensorflow/docs
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling


def reset_seed(seed=0):
    """
    Fix seed for randmize.
    """
    os.environ['PYTHONHASHSEED'] = '0'
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def norm(x, train_stats):
    """
    Normalize the data.
    """
    return (x - train_stats['mean']) / train_stats['std']


def build_model():
    """
    Build the model.
    """
    model = keras.Sequential([
        layers.Dense(64, activation='relu',
                     input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])
    return model


tky_202003 = './tph/learn/data/tokyo_20200301_20200430_utf8.csv'
tky_196002 = './tph/learn/data/tokyo_only_Feburary_1960_utf8.csv'
# tky_196002_202002 = './tph/learn/data/tokyo_only_Feburary_1960_2020_utf8.csv'
tky_196102_202002 = './tph/learn/data/tokyo_only_Feburary_1961_2020_utf8.csv'
fksm_198004 = './tph/learn/data/fukushima_19800401_19800430_utf8.csv'

# Get the data; mean temperature, mean pressure and mean humidity in the day
column_names = ['mean_t', 'mean_p', 'mean_h']
raw_dataset = pd.read_csv(tky_196102_202002, usecols=column_names)
dataset = raw_dataset.copy()
dataset.tail()

# FIXME Clean the data

# Split the data into train and test
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
# train_dataset.tail()

# Inspect the data
# sns.pairplot(train_dataset[['mean_t', 'mean_p', 'mean_h']], diag_kind='kde')


# The overall statics
train_stats = train_dataset.describe()
train_stats.pop('mean_t')
train_stats = train_stats.transpose()
# train_stats

# Split features from labels
train_labels = train_dataset.pop('mean_t')
test_labels = test_dataset.pop('mean_t')
# train_labels = train_dataset
# test_labels = test_dataset
train_labels
test_labels

# Normalize the data
normed_train_data = norm(train_dataset, train_stats)
normed_test_data = norm(test_dataset, train_stats)
normed_train_data

# Build the model
model = build_model()
# model.summary()

# Try the model.
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)
example_result

# Train the model
EPOCHS = 1000

history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split=0.2, verbose=0,
    callbacks=[tfdocs.modeling.EpochDots()])

# Visualize the model's training progress using the stats stored in the history object.
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
# hist.tail()
plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
plotter.plot({'Basic': history}, metric='mae')
plt.ylim([0, 10])
plt.ylabel('MAE [C]')
# Text(0, 0.5, 'MAE [C]')
plotter.plot({'Basic': history}, metric='mse')
plt.ylim([0, 20])
plt.ylabel('MSE [C^2]')

model = build_model()

# The pationt parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

early_history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split=0.2, verbose=0,
    callbacks=[early_stop, tfdocs.modeling.EpochDots()])

plotter.plot({'Early Stopping': early_history}, metric='mae')
plt.ylim([0, 10])
plt.ylabel('MAE [C]')

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)
print(f'Testing set Mean Abs Error: {mae:5.2f} Celsius')

# Make predictions
test_predictions = model.predict(normed_test_data).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [C]')
plt.ylabel('Predictions [C]')
lims = [0, 30]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)

# Let's talk a look at the error distribution.
error = test_predictions - test_labels
plt.hist(error, bins=25)
plt.xlabel('Prediction Error [C]')
_ = plt.ylabel('Count')
