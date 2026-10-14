import numpy as np
import matplotlib.pyplot as plt
import probas_loi


def histogramme(img):
    histo = []
    for niveau in range(256):
        histo.append(np.sum(img == niveau))
    return histo


def corriger_gris(img):
    pixels = img.flatten().tolist()

    F = probas_loi.calcul_inconnu(pixels)

    nouveaux_pixels = []
    for f in F:
        nouveaux_pixels.append(round(255 * f))

    nouveaux_pixels = np.array(nouveaux_pixels, dtype=np.uint8)
    return nouveaux_pixels.reshape(img.shape)

def corriger_couleur(img):
    resultat = np.zeros_like(img[:, :, :3])
    for canal in range(3):
        resultat[:, :, canal] = corriger_gris(img[:, :, canal])
    return resultat


def afficher(img, img_corrigee, nom):
    plt.figure(figsize=(10, 8))
    plt.suptitle(nom)

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    plt.title("Image originale")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.bar(range(256), histogramme(img), width=1)
    plt.xlim(0, 255)
    plt.title("Histogramme original")

    plt.subplot(2, 2, 3)
    plt.imshow(img_corrigee, cmap="gray", vmin=0, vmax=255)
    plt.title("Image corrigée")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.bar(range(256), histogramme(img_corrigee), width=1)
    plt.xlim(0, 255)
    plt.title("Histogramme corrigé")

    plt.tight_layout()
    plt.show()


for nom in ["chien_gris.jpg", "paysage_gris.jpg"]:
    img = plt.imread(nom)

    if img.ndim == 2:
        img_corrigee = corriger_gris(img)
        afficher(img, img_corrigee, nom)
    else:
        img_corrigee = corriger_couleur(img)
        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title("Image originale")
        plt.axis("off")
        plt.subplot(1, 2, 2)
        plt.imshow(img_corrigee)
        plt.title("Image corrigée")
        plt.axis("off")
        plt.show()

