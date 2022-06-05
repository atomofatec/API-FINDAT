import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', '']
colunas = [2, 0]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Taubaté',fontsize = 16)
plt.savefig('GraficoTaubaté.png',dpi = 600,bbox_inches = 'tight')
plt.show()
