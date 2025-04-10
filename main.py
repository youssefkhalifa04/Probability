import numpy as np
import matplotlib.pyplot as plt

# Données
x = [0, 1, 2, 3, 4, 5]
effectifs = [250, 600, 380, 120, 410, 240]
total = sum(effectifs)

# Fonction pour calculer les fréquences cumulatives
def frequences_cumulatives(effectifs):
    total = sum(effectifs)

    fc_croissante = []
    cumul = 0
    for e in effectifs:
        cumul += e
        fc_croissante.append(cumul / total)

    fc_decroissante = []
    cumul = total
    for e in effectifs:
        fc_decroissante.append(cumul / total)
        cumul -= e

    return fc_croissante, fc_decroissante

# Calcul des fréquences cumulatives
fc_crois, fc_decrois = frequences_cumulatives(effectifs)

# Utilisation de np.linspace pour avoir plus de points sur l'axe des x
x_dense = np.linspace(min(x), max(x), 1000)  # 1000 points de 0 à 5

# Courbes discontinues avec des sauts visibles (en utilisant les valeurs calculées de fc_crois et fc_decrois)
plt.step(x, fc_crois, where='post', label='Croissante', color='blue')
plt.step(x, fc_decrois, where='post', label='Décroissante', color='red')

# Ajouter des titres et labels
plt.title("Courbes discontinues des fréquences cumulatives avec linspace")
plt.xlabel("Nombre de visites")
plt.ylabel("Fréquence cumulative")
plt.legend()
plt.grid(True)
plt.show()


# --- Moyenne, variance, écart-type ---
def calcul_stats(x, effectifs):
    total = sum(effectifs)
    moyenne = sum(xi * ni for xi, ni in zip(x, effectifs)) / total
    variance = sum(ni * (xi - moyenne) ** 2 for xi, ni in zip(x, effectifs)) / total
    ecart_type = math.sqrt(variance)
    return moyenne, variance, ecart_type

moy, var, ecart = calcul_stats(x, effectifs)

print(f"Moyenne : {moy:.2f}")
print(f"Variance : {var:.2f}")
print(f"Écart-type : {ecart:.2f}")
