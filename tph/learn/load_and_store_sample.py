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
Recurrent Neural Network with Keras.
https://www.tensorflow.org/guide/keras/

Keras Documentation
https://keras.io

Weather forecasting with Recurrent Neural Networks in Python
https://medium.com/analytics-vidhya/weather-forecasting-with-recurrent-neural-networks-1eaa057d70c3

@date 1 April 2020
@author mitsuhisaT <asihustim@gmail.com>
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


tky_202003 = 'data/tokyo_20200301_20200331_utf8.csv'
tky_196002_202002 = 'data/tokyo_only_Feburary_1960_2020_utf8.csv'
fksm_198004 = 'data/fukushima_19800401_19800430_utf8.csv'

dataset = pd.resd(tky_202003)
dataset = dataset.dropna(subset=['','',])
