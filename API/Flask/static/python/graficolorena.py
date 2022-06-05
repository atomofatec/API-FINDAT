import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', 'Administração', 'Comércio']
colunas = [1, 1, 2]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Lorena',fontsize = 16)
plt.savefig('GraficoLorena.png',dpi = 600,bbox_inches = 'tight')
plt.show()
