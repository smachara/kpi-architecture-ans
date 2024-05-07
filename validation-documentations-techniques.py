import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar los datos desde un archivo CSV
data = pd.read_csv('validation-documentations-techniques.csv')

# Ordenar los datos por el orden del periodo
data.sort_values(by=['Periodo_Orden', 'Projet'], inplace=True)

# Configuración de colores para el gráfico
colors_bar = ['b', 'r', 'g', 'c', 'm', 'y', 'k']  # Colores para las barras
colors_line = ['navy', 'darkred', 'darkgreen', 'darkcyan', 'purple', 'goldenrod', 'black']  # Colores para las líneas

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(14, 7))
bar_width = 0.35 / len(data['Projet'].unique())
index = np.arange(len(data['Periodo_Texto'].unique()))

# Dibujar barras y líneas para cada proyecto
for i, projet in enumerate(data['Projet'].unique()):
    subset = data[data['Projet'] == projet]
    
    # Dibujar las barras
    ax1.bar(index + i * bar_width, subset['Documents validés'], bar_width, label=f'Docs validés {projet}', color=colors_bar[i % len(colors_bar)])
    ax1.bar(index + i * bar_width, subset['Documents en validation'], bar_width, bottom=subset['Documents validés'], label=f'Docs en validation {projet}', color=colors_bar[(i + 1) % len(colors_bar)])

# Ajustar las etiquetas y las leyendas de las barras
ax1.set_xlabel('Période')
ax1.set_ylabel('Nombre de documents')
ax1.set_title('Progression des validations des documents techniques')
ax1.set_xticks(index + bar_width * len(data['Projet'].unique()) / 2)
ax1.set_xticklabels(data['Periodo_Texto'].unique())
ax1.legend(loc='upper left', bbox_to_anchor=(1.04, 1), borderaxespad=0)

# Añadir y configurar el eje para el porcentaje de avance
ax2 = ax1.twinx()
ax2.set_ylabel('% Avancement')

# Dibujar las líneas para el porcentaje de avance
for i, projet in enumerate(data['Projet'].unique()):
    subset = data[data['Projet'] == projet]
    ax2.plot(index + i * bar_width + bar_width / 2, subset['% Avancement'], 'o-', color=colors_line[i % len(colors_line)], label=f'% Avancement {projet}')

# Ajustar las leyendas de las líneas
ax2.legend(loc='upper right', bbox_to_anchor=(1.04, 0.8), borderaxespad=0)

plt.show()
