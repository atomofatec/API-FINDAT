import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', 'Comércio', 'Engenharia', 'Contabilidade']
colunas = [10, 2, 1, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('São José dos Campos',fontsize = 16)
plt.savefig('GraficoSJC.png',dpi = 600,bbox_inches = 'tight')
plt.show()
