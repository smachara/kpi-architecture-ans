import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar los datos desde un archivo CSV
data = pd.read_csv('avancement-release.csv')

# Ordenar los datos por el orden del periodo, proyecto y release
data.sort_values(by=['Periodo_Orden', 'Projet', 'Release'], inplace=True)

# Configuración de colores para el gráfico
colors_line = ['navy', 'darkred', 'darkgreen', 'darkcyan', 'purple', 'goldenrod', 'black', 'orange', 'brown', 'blue']  # Asegúrate de tener suficientes colores

# Crear el gráfico
fig, ax = plt.subplots(figsize=(14, 7))
index = np.arange(len(data['Periodo_Texto'].unique()))

# Dibujar líneas para cada combinación de proyecto y release
for i, (proj, rel) in enumerate(data.groupby(['Projet', 'Release'])):
    proj_name, release_name = proj
    ax.plot(index, rel['Pourcentage d\'Avancement'], 'o-', color=colors_line[i % len(colors_line)], label=f'{proj_name} - {release_name}')

# Ajustar las etiquetas y las leyendas
ax.set_xlabel('Période')
ax.set_ylabel('% Avancement par release')
ax.set_title('Pourcentage d\'avancement par release et projet')
ax.set_xticks(index)
ax.set_xticklabels(data['Periodo_Texto'].unique())
ax.legend(loc='upper left', bbox_to_anchor=(1.04, 1), borderaxespad=0)

plt.show()
