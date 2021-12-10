import random

import json

import pickle

import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer #Essa função serve para reduzir a palavra a sua forma canonica.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lematizador = WordNetLemmatizer #Recebe a função para reduzir a palavra a sua forma canonica

intents = json.loads(open('intents.JSON').read()) #Carregar o dicionario para a variavel intents

palavras = []
classes = []
documentos = []
ignore_letters = ['?', '!', '.', ','] #Caracteres que não serão levados em conta pela "leitura" das entradas