import matplotlib.pyplot as plt
import numpy as np

labels = ['Atendente', 'Administração', 'Engenharia']
colunas = [1, 2, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Guaratinguetá',fontsize = 16)
plt.savefig('GraficoGuaratinguetá.png',dpi = 600,bbox_inches = 'tight')
plt.show()
