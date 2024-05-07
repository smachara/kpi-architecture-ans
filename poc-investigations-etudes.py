import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cargar los datos desde un archivo CSV
data = pd.read_csv('poc-investigations-etudes.csv')

# Ordenar los datos por el orden del periodo y el proyecto
data.sort_values(by=['Periodo_Orden', 'Projet'], inplace=True)

# Configuración de colores para el gráfico
colors_finished = ['navy', 'darkgreen']  # Colores para las barras de sujetos adressés
colors_ongoing = ['lightblue', 'lightgreen']  # Colores para las barras de sujetos en cours

# Crear el gráfico
fig, ax = plt.subplots(figsize=(14, 7))
bar_width = 0.35 / len(data['Projet'].unique())
index = np.arange(len(data['Periodo_Texto'].unique()))

# Dibujar barras para cada proyecto
for i, projet in enumerate(data['Projet'].unique()):
    subset = data[data['Projet'] == projet]
    
    # Dibujar las barras de sujetos adressés
    ax.bar(index + i * bar_width, subset['Nombre de sujets adressés'], bar_width, label=f'Sujets adressés {projet}', color=colors_finished[i % len(colors_finished)])
    # Dibujar las barras de sujetos en cours encima
    ax.bar(index + i * bar_width, subset['Nombre de sujets en cours'], bar_width, bottom=subset['Nombre de sujets adressés'], label=f'Sujets en cours {projet}', color=colors_ongoing[i % len(colors_ongoing)])

# Ajustar las etiquetas y las leyendas de las barras
ax.set_xlabel('Période')
ax.set_ylabel('Nombre de sujets')
ax.set_title('Progression des POC, Investigations et Études par Projet')
ax.set_xticks(index + bar_width * len(data['Projet'].unique()) / 2)
ax.set_xticklabels(data['Periodo_Texto'].unique())
ax.legend(loc='upper left', bbox_to_anchor=(1.04, 1), borderaxespad=0)

plt.show()
