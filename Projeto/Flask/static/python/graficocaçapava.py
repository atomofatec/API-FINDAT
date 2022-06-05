import matplotlib.pyplot as plt
import numpy as np

labels = ['Comércio', 'Enfermagem', 'Administração', 'Engenharia']
colunas = [2, 1, 2, 1]

plt.bar(labels,colunas,color = 'midnightblue')
plt.ylabel('nº vagas',fontsize = 12)
plt.title('Caçapava',fontsize = 16)
plt.savefig('GraficoCacapava.png',dpi = 600,bbox_inches = 'tight')
plt.show()
