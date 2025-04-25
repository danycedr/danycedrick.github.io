import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Tous les packages ont été importés avec succès ✅")

# Remplace par le nom exact de ton fichier
dff = pd.read_csv('US_Accidents_March23.csv', nrows=1000)
print(dff.head())

print("dany")
# 🔍 Analyse descriptive
#1. Quel est le jour de la semaine avec le plus d’accidents ?
dff
