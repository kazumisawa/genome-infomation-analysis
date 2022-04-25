import numpy as np
import matrixReLU as m

def maximumMatchMatrix(S, d):
    K = np.zeros_like(S)
    len1, len2 = K.shape
    #最初の行と最初の列以外は隣を利用
    compare = np.zeros(3)
    for j in range(len2):
        for i in range(len1):
            compare[0] = K[i-1, j-1] + S[i,j]
            compare[1] = L[i-1, j  ] - d
            compare[2] = K[i,   j-1] - d
            K[i,j] = np.max(m.matrixReLU(compare))
    return K
