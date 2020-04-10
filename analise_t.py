import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ACURACIA = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Análise T/resultado_T_A.csv')
KAPPA = pd.read_csv('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Análise T/resultado_T_K.csv')

porcentagem = ['50', '100', '150', '200', '250', '300']
cor = ['red', 'green', 'blue', 'orange', 'black', 'pink']

labels = ['0.0','0.05', '0.1', '0.15', '0.2','0.25']

plt.rcParams['figure.figsize'] = (12,5)
fig, axs = plt.subplots(1, 2)
fig.subplots_adjust(left=0.07, bottom=0.135, right=0.98, top=0.93, wspace=0.22, hspace=0.45)

x = np.arange(5)+1
for i,c in enumerate(porcentagem):     
    y_acc = ACURACIA[c]
    ax1 = axs[0]
    ax1.plot(x,y_acc, color=cor[i], label='Labeled '+c)
    #ax1.fill_between(x, y_acc - resultado['DPA'], y_acc + resultado['DPA'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax1.set_title('ACCURACY', fontsize=24)
    ax1.set_xlabel('t value', fontsize=22)
    ax1.set_ylim(0., 1, 0.1)
    #ax1.set_xlim(1, 6, 1)
    #ax1.set_xticks(np.arange(5))
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.set_xticklabels(labels)
    ax1.legend()
       
    y_rec = KAPPA[c]
    ax2 = axs[1]
    ax2.plot(x,y_rec, color=cor[i], label='Labeled '+c)
    #ax2.fill_between(x, y_rec - resultado['DPK'], y_rec + resultado['DPK'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax2.set_title('KAPPA', fontsize=24)
    ax2.set_xlabel('t value', fontsize=22)
    ax2.set_ylim(0., 1, 0.1)
    #ax2.set_xticks(np.arange(5))
    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax2.set_xticklabels(labels)
    ax2.legend()

plt.savefig('D:/Drive UFRN/Doutorado/Resultados/Artigo GRRS/Análise T/resultado_T.eps', dpi=300)