import matplotlib.pyplot as plt
import numpy as np

labels = ['TI / Informática', 'Educação', 'Técnico de Serviços']
colunas = [1, 1, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Jacareí',fontsize = 16)
plt.savefig('GraficoJacareí.png',dpi = 600,bbox_inches = 'tight')
plt.show()
