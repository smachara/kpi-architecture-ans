import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar los datos desde un archivo CSV
data = pd.read_csv('validation-documentations-techniques.csv')

# Ordenar los datos por el orden del periodo
data.sort_values(by=['Periodo_Orden', 'Projet'], inplace=True)

# Configuración de colores para el gráfico
warm_colors = ['red', 'orange', 'yellow', 'darkred', 'coral', 'gold', 'darkorange']  # Colores cálidos para documentos validados
cool_colors = ['blue', 'cyan', 'purple', 'darkblue', 'deepskyblue', 'darkviolet', 'steelblue']  # Colores fríos para documentos en validación
line_colors = ['navy', 'darkred', 'darkgreen', 'darkcyan', 'purple', 'goldenrod', 'black']  # Colores para las líneas de avance

# Crear el gráfico
fig, ax1 = plt.subplots(figsize=(14, 7))
bar_width = 0.35 / len(data['Projet'].unique())
index = np.arange(len(data['Periodo_Texto'].unique()))

# Dibujar barras y líneas para cada proyecto
for i, projet in enumerate(data['Projet'].unique()):
    subset = data[data['Projet'] == projet]
    
    # Dibujar las barras
    ax1.bar(index + i * bar_width, subset['Documents validés'], bar_width, label=f'Docs validés {projet}', color=warm_colors[i % len(warm_colors)])
    ax1.bar(index + i * bar_width, subset['Documents en validation'], bar_width, bottom=subset['Documents validés'], label=f'Docs en validation {projet}', color=cool_colors[i % len(cool_colors)])

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
    ax2.plot(index + i * bar_width + bar_width / 2, subset['% Avancement'], 'o-', color=line_colors[i % len(line_colors)], label=f'% Avancement {projet}')

# Ajustar las leyendas de las líneas
ax2.legend(loc='upper right', bbox_to_anchor=(1.04, 0.8), borderaxespad=0)

plt.show()