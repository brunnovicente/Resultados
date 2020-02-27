"""
D:\Drive UFRN\Doutorado\Resultados\Artigo GRRS\Experimentos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, cohen_kappa_score

resultado = pd.DataFrame()
acuracia = []
kappa = []
dpa = []
dpk = []

modelos = ['MLP', 'KNN', 'SVM', 'RF', 'NB', 'LR']

for 