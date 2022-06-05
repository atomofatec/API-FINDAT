import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', 'Atendente', 'Comunicação']
colunas = [1, 1, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Aparecida',fontsize = 16)
plt.savefig('GraficoAparecida.png',dpi = 600,bbox_inches = 'tight')
plt.show()
