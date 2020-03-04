import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TRANSDUTIVO = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/resultado_transdutivo.csv')
INDUTIVO = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Analise Final/resultado_indutivo.csv')

porcentagem = ['50', '100', '150', '200', '250', '300']
cor = ['red', 'green', 'blue', 'orange', 'black', 'pink']

ACURACIA = TRANSDUTIVO[porcentagem].T
plt.rcParams['figure.figsize'] = (12,5)
fig, axs = plt.subplots(1, 2)
fig.subplots_adjust(left=0.07, bottom=0.120, right=0.98, top=0.93, wspace=0.22, hspace=0.45)

nomes = TRANSDUTIVO['MODELO'].values

x = np.arange(6)+1
for i in np.arange():
    y_acc = ACURACIA[c]
    ax1 = axs[0]
    ax1.plot(x,y_acc, color=cor[i], label='Labeled '+c)
    #ax1.fill_between(x, y_acc - resultado['DPA'], y_acc + resultado['DPA'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax1.set_title('Accuracy', fontsize=16)
    ax1.set_xlabel('K', fontsize=14)
    ax1.set_ylim(0., 1, 0.1)
    #ax1.set_xlim(0.1,25.1)
    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax1.legend()
       
    y_rec = KAPPA[c]
    ax2 = axs[1]
    ax2.plot(x,y_rec, color=cor[i], label='Labeled '+c)
    #ax2.fill_between(x, y_rec - resultado['DPK'], y_rec + resultado['DPK'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax2.set_title('KAPPA', fontsize=16)
    ax2.set_xlabel('K', fontsize=14)
    ax2.set_ylim(0., 1, 0.1)
    #ax2.set_xlim(0.1,25.1)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax2.legend()

plt.savefig('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Análise T/resultado_T.eps', dpi=300)