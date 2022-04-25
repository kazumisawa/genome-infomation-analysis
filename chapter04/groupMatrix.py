import numpy as np
import scoreMatrix as sc

def groupMatrix( g1, r1, g2, r2 ):
    S = np.zeros( ( r1[1]-r1[0], r2[1]-r2[0] ) )
    m, n = len( g1 ), len( g2 )
    for i in range(m):
        for j in range(n):
            S += sc.scoreMatrix( g1[i], r1, g2[j], r2 )
    return S/(m*n)
