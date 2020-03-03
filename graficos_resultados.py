import os
import pandas as pd
import numpy as np

pastaT = 'C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise IND/'
pastaI = 'C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise TRAN/'

caminhosT = [os.path.join(pastaT, nome) for nome in os.listdir(pastaT)]
caminhosI = [os.path.join(pastaI, nome) for nome in os.listdir(pastaI)]

nomes = ['Co-training - KNN', 
         'Co-training - LR', 
         'Co-training - MLP',
         'Co-training - NB',
         'Co-training - RF',
         'Co-training - SVM',
         'SEEDED K-means',
         'Proposed Model', 
         'Self-Training - KNN', 
         'Self-Training - lR', 
         'Self-Training - MLP', 
         'Self-Training - NB', 
         'Self-Training - RF', 
         'Self-Training - SVM',
         'Tri-Training - KNN', 
         'Tri-Training - LR',
         'Tri-Training - MLP',
         'Tri-Training - NB',
         'Tri-Training - RF',
         'Tri-Training - SVM']

#resultado = pd.DataFrame()

info = []
colunas = ['MODELO','50','D50', '100','D100', '150','D150', '200','D200', '250','D250', '300','D300']
for i, caminho in enumerate(caminhosT):
    
    dados = pd.read_csv(caminho)
    acuracia = np.round(dados['ACURACIA'].values, 3)
    dpa = np.round(dados['DPA'].values, 3)
    kappa = np.round(dados['KAPPA'].values, 3)
    dpk = np.round(dados['DPK'].values, 3)
    
    linha_acuracia = []
    linha_acuracia.append(nomes[i])
    for i, a in enumerate(acuracia):
        linha_acuracia.append(a)
        linha_acuracia.append(dpa[i])
    info.append(linha_acuracia)

resultado = pd.DataFrame(info, columns=colunas)
resultado.to_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise Final/resultado_transdutivo.csv', index=False)
    
    