import math
import numpy as np
import matplotlib.pyplot as plt


def uk_vk(A, k):
    U, S, Vt = np.linalg.svd(A)
    
    uk = U[:, :k]
    vk = Vt[:k, :]
    sk = S[:k]
    
    return uk, vk, sk
    
def approx_err_epsilon(A, epsilon):
    U, S, Vt = np.linalg.svd(A)
    r = len(S)
    
    frobenius = np.sum(sigma)
    
    k = r
    while(frobenius <= epsilon):
        k -= 1
        frobenius = np.sum(sigma)
    


def main():
    img = plt.imread("paysage.jpg")

    #Taille

    shape = img.shape
    w = img.shape[0]
    h = img.shape[1]
    size = img.nbytes
    print(shape)
    print(f"{w}*{h}")
    print(size)
    
    A = img.astype(np.float32)
    
if __name__ == "__main__":
    main()
    
    
    
