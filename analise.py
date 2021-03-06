"""
D:\Drive UFRN\Doutorado\Resultados\Artigo GRRS\Experimentos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, cohen_kappa_score



modelos = ['MLP', 'KNN', 'SVM', 'RF', 'NB', 'LR']
porcentagem = [50,100,150,200,250,300]

tabela = pd.DataFrame()
tabela['P'] = porcentagem
acuracia = []
kappa = []
dpa = []
dpk = []

for i, p in enumerate(porcentagem):
    
    resultado = pd.read_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Resultados Modelo/resultado_MODELO_I_'+str(p)+'.csv')
    
    acu = []
    kap = []    
    
    for k in np.arange(10)+1:
        y_des = resultado['y'+str(k)]
        y_pre = resultado['exe'+str(k)]
            
        acu.append(accuracy_score(y_des, y_pre))
        kap.append(cohen_kappa_score(y_des, y_pre))
    
    acuracia.append(np.round(np.mean(acu), 3))
    kappa.append(np.round(np.mean(kap), 3))
    dpa.append(np.std(acuracia))
    dpk.append(np.std(kappa))
    
tabela['ACURACIA'] = acuracia
tabela['DPA'] = dpa
tabela['KAPPA'] = kappa
tabela['DPK'] = dpk

tabela.to_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise/RESULTADO_MODELO_INDUTIVO.csv', index=False)