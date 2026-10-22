import math
import numpy as np
import matplotlib.pyplot as plt


def uk_vk(A, k):
    U, S, Vt = np.linalg.svd(A)
    
    uk = U[:, :k]
    vk = Vt[:k, :]
    sk = S[:k]
    sk_vect = np.nonzero(sk)
    
    return uk, vk, sk_vect
    
    
    


def main():
    img = plt.imread("paysage.jpg")

    #Taille

    shape = img.shape
    w = img.shape[0]
    h = img.shape[1]
    size = img.nbytes
    
    
