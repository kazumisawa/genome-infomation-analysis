import numpy as np

def maximumMatchMatrix(S, d):
    F0 = np.zeros_like(S)
    len1, len2 = S.shape
    add1 = np.array(list(range(len2)))*(-d)-d
    add2 = np.array(list(range(len1+1)))*(-d)
    F1 = np.insert(F0, 0, add1, axis=0)
    F  = np.insert(F1, 0, add2, axis=1)
    compare = np.zeros(3)
    for j in range(len2):
        for i in range(len1):
            compare[0] = F[i,  j  ] + S[i,j]
            compare[1] = F[i,  j+1] - d
            compare[2] = F[i+1,j  ] - d
            F[i+1,j+1] = np.max(compare)
    return F
