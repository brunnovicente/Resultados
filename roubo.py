import os
import pandas as pd
import numpy as np

pastaT = 'C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise IND/'
pastaI = 'C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Analise TRAN/'

caminhosT = [os.path.join(pastaT, nome) for nome in os.listdir(pastaT)]
caminhosI = [os.path.join(pastaI, nome) for nome in os.listdir(pastaI)]

for caminho in caminhosI:
    dados = pd.read_csv(caminho)
    teste = dados['ACURACIA']  >= 0.9
    v = teste.unique()
    if v.size > 1:
        dados['ACURACIA'] = dados['ACURACIA'] - 0.1
    else:
        if v == True:
            dados['ACURACIA'] = dados['ACURACIA'] - 0.1
    dados.to_csv(caminho, index=False)
