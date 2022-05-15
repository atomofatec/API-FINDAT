import matplotlib.pyplot as plt
import numpy as np

labels = ['TI', 'Logística', 'Marketing', 'Educação', 'Técnico', 'Engenharia', 'Contabilidade']
colunas = [2, 2, 2, 2, 1, 1, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Vagas por Área profissional',fontsize = 16)
plt.savefig('GraficoVagasArea.png',dpi = 600,bbox_inches = 'tight')
plt.show()
