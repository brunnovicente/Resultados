import os
import pandas as pd
import numpy as np

pastaT = 'D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise IND/'
pastaI = 'D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise TRAN/'

caminhosT = [os.path.join(pastaT, nome) for nome in os.listdir(pastaT)]
caminhosI = [os.path.join(pastaI, nome) for nome in os.listdir(pastaI)]

tabela = pd.DataFrame()

for caminho in caminhosT:
    
    dados = pd.read_csv(caminho)
    acuracia = np.round(dados['KAPPA'].values, 3)
    dpa = np.round(dados['DPK'].values, 3)
    
    linha = []
    for i, a in enumerate(acuracia):
        linha.append(str(a)+' $\pm$ '+str(dpa[i]))
    
    nome = caminho.split('/')
    tabela[nome[-1]] = linha

tabela = tabela.T
tabela.to_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/tabela_kappa_T.csv')

tabela1 = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/tabela_acuracia_I.csv')
tabela2 = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/tabela_kappa_I.csv')

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

colunas = tabela1.columns.values
colunas = colunas[1:]
nomes_colunas = ['50', '100' , '150', '200', '250', '300']

resultado1 = pd.DataFrame()
resultado1['MODELOS'] = nomes
for i,c in enumerate(colunas):
    resultado1[nomes_colunas[i]] = tabela1[c]

resultado2 = pd.DataFrame()
resultado2['MODELOS'] = nomes
for i,c in enumerate(colunas):
    resultado2[nomes_colunas[i]] = tabela2[c]

resultado = pd.concat([resultado1, resultado2])
resultado.to_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/tabela_indutivo.csv', index=False)