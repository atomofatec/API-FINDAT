import matplotlib.pyplot as plt
import numpy as np

labels = ['SJC', 'Jambeiro', 'Jacareí', 'Taubaté', 'Home Office']
colunas = [5, 1, 4, 2, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Vagas por Cidades',fontsize = 16)
plt.savefig('GraficoVagasCidade.png',dpi = 600,bbox_inches = 'tight')
plt.show()
