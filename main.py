import math
import numpy as np
import matplotlib.pyplot as plt
import probas_loi

img = plt.imread("chien_gris.jpg")

def histogramme_gris(img):
    w, h = img.shape
    histo = []

    for i in range(w):
        for j in range(h):
            histo.append(img[i][j])

    return histo

histo = histogramme_gris(img)
calc_inconnu(histo)
