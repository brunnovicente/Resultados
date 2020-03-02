import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, cohen_kappa_score

porcentagem = [50, 100, 150, 200, 250, 300]
cor = ['red', 'green', 'blue', 'orange', 'black', 'pink']

plt.rcParams['figure.figsize'] = (12,5)
fig, axs = plt.subplots(1, 2)
fig.subplots_adjust(left=0.07, bottom=0.120, right=0.98, top=0.93, wspace=0.22, hspace=0.45)

for c, p in enumerate(porcentagem):
    print('Porcentagem: '+str(p))
    resultado = pd.DataFrame()
    acuracia = []
    kappa = []
    dpa = []
    dpk = []
    
    for i in np.arange(25)+1:

        dados = pd.read_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Resultados Analise K/resultado_'+str(p)+'k'+str(i)+'.csv')
        
        acu = []
        kap = []
        
        for j in np.arange(10)+1:
            y = dados['y'+str(j)]
            yp = dados['exe'+str(j)]
            a = accuracy_score(y, yp)
            k = cohen_kappa_score(y, yp)
            acu.append(a)
            kap.append(k)
        
        acuracia.append(np.mean(acu))
        kappa.append(np.mean(kap))
        dpa.append(np.std(acu))
        dpk.append(np.std(kap))
    
    resultado['k'] = np.arange(25)+1
    resultado['ACURACIA'] = np.round(acuracia, 3)
    resultado['DPA'] = np.round(dpa, 3)
    resultado['KAPPA'] = np.round(kappa, 3)
    resultado['DPK'] = np.round(dpk, 3)
    
    resultado.to_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Análise K/resultado_k_'+str(p)+'.csv', index=False)
    
    
    estilos = ['-','-','-','-','-']
    marcador = ['','','','','']
    nome = ['MNIST', 'MNIST64','Fashion MNIST','USPS', 'PENDIGITS']
              
    x = np.arange(25)+1
     
    y_acc = resultado['ACURACIA']
    ax1 = axs[0]
    ax1.plot(x,y_acc, color=cor[c], label='Labeled '+str(p))
    #ax1.fill_between(x, y_acc - resultado['DPA'], y_acc + resultado['DPA'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax1.set_title('Accuracy', fontsize=16)
    ax1.set_xlabel('K', fontsize=14)
    ax1.set_ylim(0., 1, 0.1)
    ax1.set_xlim(0.1,25.1)
    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax1.legend()
       
    y_rec = resultado['KAPPA']
    ax2 = axs[1]
    ax2.plot(x,y_rec, color=cor[c], label='Labeled '+str(p))
    #ax2.fill_between(x, y_rec - resultado['DPK'], y_rec + resultado['DPK'], alpha=0.25, facecolor=cor[c], antialiased=True)
    ax2.set_title('KAPPA', fontsize=16)
    ax2.set_xlabel('K', fontsize=14)
    ax2.set_ylim(0., 1, 0.1)
    ax2.set_xlim(0.1,25.1)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax2.legend()
        
    #ax1.legend(bbox_to_anchor=(1.2, -0.2), ncol=5, fontsize=14)

plt.savefig('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/Análise K/resultado_k.eps', dpi=300)
plt.show()