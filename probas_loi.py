import math
import random
import matplotlib.pyplot as plt

#Pour le remettre sous la forme d'une loi uniforme, il faut y appliquer la fonction quantile de la loi exponentielle

def f(x, l):
    return 1 - math.exp(-l * x)

def calc_param(x, l):
    return -math.log(1-x)/l

def calc_exponentielle(N, l):
    tab = [0]*N
    for i in range(N):
        x = random.random()
        tab[i] = calc_param(x, l)
    return tab

def calc_uniforme(N, l):
    tab = []
    ex = calc_exponentielle(N, l)
    for i in range(N):
        x = random.random()
        tab.append(f(ex[i], l))
    return tab

def calcul_inconnu(echantillon):
    s_ech = sorted(echantillon)
    tab = []
    N = len(s_ech)
    print(N)
    for i, _  in enumerate(s_ech, start=1):
        tab.append(i/N)
    return tab

tab = calc_exponentielle(10000, 2)
tab2 = calc_uniforme(100000, 2)
tab3 = calcul_inconnu(calc_exponentielle(10000, 2))
plt.hist(tab3)
plt.show()
