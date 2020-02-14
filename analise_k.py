import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, cohen_kappa_score

resultado = pd.DataFrame()
acuracia = []
kappa = []
dpa = []
dpk = []

for i in np.arange(100)+1:
    
    dados = pd.read_csv('C:/Users/brunn/Google Drive/Doutorado/Resultados/Artigo GRRS/resultado_k'+str(i)+'.csv')
    
    acu = []
    kap = []
    
    for i in np.arange(10)+1:
        y = dados['y'+str(i)]
        yp = dados['exe'+str(i)]
        a = accuracy_score(y, yp)
        k = cohen_kappa_score(y, yp)
        acu.append(a)
        kap.append(k)
    
    acuracia.append(np.mean(acu))
    kappa.append(np.mean(kap))
    dpa.append(np.std(acu))
    dpk.append(np.std(kap))
    
resultado['ACURACIA'] = np.round(acuracia, 3)
resultado['DPA'] = np.round(dpa, 3)
resultado['KAPPA'] = np.round(kappa, 3)
resultado['DPK'] = np.round(dpk, 3)

estilos = ['-','-','-','-','-']
marcador = ['','','','','']
nome = ['MNIST', 'MNIST64','Fashion MNIST','USPS', 'PENDIGITS']

plt.rcParams['figure.figsize'] = (12,5)
fig, axs = plt.subplots(1, 2)
fig.subplots_adjust(left=0.07, bottom=0.12, right=0.98, top=0.93, wspace=0.22, hspace=0.45)
   
x = np.arange(100)+1
 
y_acc = resultado['ACURACIA']
ax1 = axs[0]
ax1.plot(x,y_acc, color='red')
ax1.fill_between(x, y_acc - resultado['DPA'], y_acc + resultado['DPA'], alpha=0.25, facecolor='red', antialiased=True)
ax1.set_title('ACURÁCIA', fontsize=16)
ax1.set_xlabel('Valor de K', fontsize=14)
ax1.set_ylim(0.7, 1, 0.1)
ax1.set_xlim(0,100)
ax1.tick_params(axis='both', which='major', labelsize=15)

y_rec = resultado['KAPPA']
ax2 = axs[1]
ax2.plot(x,y_rec, color='blue')
ax2.fill_between(x, y_rec - resultado['DPK'], y_rec + resultado['DPK'], alpha=0.25, facecolor='blue', antialiased=True)
ax2.set_title('KAPPA', fontsize=16)
ax2.set_xlabel('Valor de K', fontsize=14)
ax2.set_ylim(0.7, 1, 0.1)
ax2.set_xlim(1,100)
ax2.tick_params(axis='both', which='major', labelsize=15)
    
#ax1.legend(bbox_to_anchor=(0.7, -0.2), ncol=5, fontsize=14)

#plt.savefig('resultado_k.eps', dpi=300)
plt.show()


#resultado.to_csv('analise_k'+str(i)+'.csv', index=False)