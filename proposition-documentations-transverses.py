import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos desde un archivo CSV
data = pd.read_csv('proposition-documentations-transverses.csv')

# Extracción de los datos para el gráfico
labels = data['Type de Document']
sizes = data['Nombre']

# Colores para cada segmento del gráfico
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple', 'orange']

# Crear el gráfico de camembert
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)

# Igualar aspecto para que se dibuje como un círculo
ax.axis('equal')

# Título del gráfico
plt.title('Répartition des Types de Documentations Transverses ANS')

# Mostrar el gráfico
plt.show()
