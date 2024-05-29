import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Lire les données à partir d'un fichier CSV
file_path = 'taux_de_validation.csv'  # Remplacez par le chemin de votre fichier CSV
df = pd.read_csv(file_path, parse_dates=['Date'])

# Obtenir les noms des projets
projects = df['Project'].unique()

# Créer des pivots pour les données demandées et validées
pivot_requested = df.pivot(index='Date', columns='Project', values='Requested')
pivot_validated = df.pivot(index='Date', columns='Project', values='Validated')

# Calculer les totaux cumulés
df['Total Requested'] = df.groupby('Date')['Requested'].transform('sum')
df['Total Validated'] = df.groupby('Date')['Validated'].transform('sum')

total_requested = df.groupby('Date')['Total Requested'].first()
total_validated = df.groupby('Date')['Total Validated'].first()

# Préparer les données pour le graphique
dates = df['Date'].drop_duplicates().sort_values()
date_labels = dates.dt.strftime('%Y-%m')

# Créer le graphique en 2D
fig, ax = plt.subplots(figsize=(12, 8))

lines = []
labels = []

# Tracer les données pour chaque projet
for project in projects:
    line_requested, = ax.plot(dates, pivot_requested[project], marker='x', linestyle='--', label=f'{project} - Requested')
    line_validated, = ax.plot(dates, pivot_validated[project], marker='o', label=f'{project} - Validated')
    lines.append(line_requested)
    lines.append(line_validated)
    labels.append(f'{project} - Requested')
    labels.append(f'{project} - Validated')

# Tracer les totaux cumulés
line_total_requested, = ax.plot(dates, total_requested, marker='x', linestyle='-', color='black', label='Total Requested')
line_total_validated, = ax.plot(dates, total_validated, marker='o', linestyle='-', color='grey', label='Total Validated')
lines.append(line_total_requested)
lines.append(line_total_validated)
labels.append('Total Requested')
labels.append('Total Validated')

# Paramétrer les étiquettes et les axes
ax.set_xlabel('Date')
ax.set_ylabel('Nombre de Livrables')
ax.set_xticks(dates)
ax.set_xticklabels(date_labels, rotation=45, ha='right')

plt.title('Livrables Demandés vs Validés (Août 2023 - Mai 2024)')
ax.legend()

# Créer les boutons de sélection
rax = plt.axes([0.02, 0.4, 0.15, 0.45])
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)

# Fonction de mise à jour de la visibilité des lignes
def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(func)

plt.show()
