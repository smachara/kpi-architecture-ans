import pandas as pd
import matplotlib.pyplot as plt

# Lire les données à partir d'un fichier CSV
file_path = 'repartition_activites_par_type.csv'  # Remplacez par le chemin de votre fichier CSV
df = pd.read_csv(file_path)

# Créer le graphique de tarte
plt.figure(figsize=(8, 8))
plt.pie(df['Nombre d\'Activités'], labels=df['Activité'], autopct='%1.1f%%', startangle=140)
plt.title('Répartition des Activités par Type \n 08/2023-05/2024')
plt.show()