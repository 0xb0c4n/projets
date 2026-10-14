import math
import random
import matplotlib.pyplot as plt


def F_exp(x, l):
    return 1 - math.exp(-l * x)


def exp_reciproque(u, l):
    return -math.log(1 - u) / l


def exponentielle(N, l):
    echantillon = []
    for i in range(N):
        u = random.random()
        echantillon.append(exp_reciproque(u, l))
    return echantillon


def uniforme(echantillon, l):
    resultat = []
    for x in echantillon:
        resultat.append(F_exp(x, l))
    return resultat


def calcul_inconnu(echantillon):
    N = len(echantillon)
    valeurs_triees = sorted(echantillon)

    proportion = {}
    for i in range(N):
        proportion[valeurs_triees[i]] = (i + 1) / N

    resultat = []
    for x in echantillon:
        resultat.append(proportion[x])
    return resultat


if __name__ == "__main__":
    N = 10000
    l = 2

    ech_expo = exponentielle(N, l)

    ech_uniforme = uniforme(ech_expo, l)

    ech_inconnu = calcul_inconnu(ech_expo)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.hist(ech_expo, bins=50, density=True)
    plt.title("Loi exponentielle E(" + str(l) + ")")

    plt.subplot(1, 3, 2)
    plt.hist(ech_uniforme, bins=50, density=True)
    plt.title("Après F_X (loi connue)")

    plt.subplot(1, 3, 3)
    plt.hist(ech_inconnu, bins=50, density=True)
    plt.title("Après F (loi inconnue)")

    plt.tight_layout()
    plt.show()
