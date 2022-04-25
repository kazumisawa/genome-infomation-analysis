import numpy as np

def affineGapMatchMatrix(S, u, v):
    s = S.shape
    len1, len2 = S.shape
    add1 = np.array(list(range(len2)))*(-v)-v
    add2 = np.array(list(range(len1+1)))*(-v)
    F0 = np.zeros_like(S)
    F1 = np.insert(F0, 0, add1, axis=0)
    F  = np.insert(F1, 0, add2, axis=1)

    P, Q  = F.copy(), F.copy()
    compare = np.zeros(3)
    for i in range(len1):
        for j in range(len2):
            P[i+1, j+1] = max( F[i,j+1]-u, P[i,j+1]-v )
            Q[i+1, j+1] = max( F[i+1,j]-u, Q[i+1,j]-v )
            compare[0] = F[i,   j  ] + S[i,j]
            compare[1] = P[i,   j+1]
            compare[2] = Q[i+1, j  ]
            F[i+1,j+1] = np.max(compare)
    return F, P, Q
