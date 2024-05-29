import pandas as pd
import matplotlib.pyplot as plt

# Lire les données à partir d'un fichier CSV
file_path = 'taux_de_validation.csv'  # Remplacez par le chemin de votre fichier CSV
df = pd.read_csv(file_path, parse_dates=['Date'])

# Calculer le taux de validation pour chaque projet et chaque mois
df['Validation Rate (%)'] = (df['Validated'] / df['Delivered']) * 100

# Pivot de la table pour avoir les projets en colonnes
pivot_df = df.pivot(index='Date', columns='Project', values='Validation Rate (%)')

# Calculer le taux de validation total par mois
pivot_df['Total Validation Rate (%)'] = pivot_df.mean(axis=1)

# Calculer les livrables demandés vs validés
df['Requested vs Validated'] = df['Validated'] / df['Requested']

# Pivot de la table pour les livrables demandés vs validés
pivot_requested_validated = df.pivot(index='Date', columns='Project', values='Requested vs Validated')

# Tracer les taux de validation pour les deux projets avec les totaux par mois
plt.figure(figsize=(12, 6))
plt.plot(pivot_df.index, pivot_df['Project 1'], marker='o', label='Project 1 - Validation Rate')
plt.plot(pivot_df.index, pivot_df['Project 2'], marker='o', label='Project 2 - Validation Rate')
plt.plot(pivot_df.index, pivot_df['Total Validation Rate (%)'], marker='o', linestyle='--', label='Total Validation Rate')

plt.axhline(y=100, color='r', linestyle='--', label='Target Validation Rate')

plt.title('Taux de Validation des Livrables (Août 2023 - Mai 2024)')
plt.xlabel('Date')
plt.ylabel('Taux de Validation (%)')
plt.ylim(0, 110)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Tracer les livrables demandés vs validés pour les deux projets
plt.figure(figsize=(12, 6))
plt.plot(pivot_requested_validated.index, pivot_requested_validated['Project 1'], marker='o', label='Project 1 - Requested vs Validated')
plt.plot(pivot_requested_validated.index, pivot_requested_validated['Project 2'], marker='o', label='Project 2 - Requested vs Validated')

plt.axhline(y=1, color='r', linestyle='--', label='Target Requested vs Validated (1.0)')

plt.title('Livrables Demandés vs Validés (Août 2023 - Mai 2024)')
plt.xlabel('Date')
plt.ylabel('Requested vs Validated')
plt.ylim(0, 1.2)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
