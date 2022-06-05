import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', 'Marketing']
colunas = [1, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Home Office',fontsize = 16)
plt.savefig('GraficoHomeOffice.png',dpi = 600,bbox_inches = 'tight')
plt.show()

