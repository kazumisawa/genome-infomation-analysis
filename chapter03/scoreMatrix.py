import numpy as np
import score

def scoreMatrix( seq1, range1, seq2, range2 ):
    start1, end1 = range1
    start2, end2 = range2
    #score matrix
    m, n = end1-start1, end2-start2
    S = np.zeros( ( m, n ) )
    for i in range(m):
        x = i + start1
        for j in range(n):
            y = j + start2
            S[i, j] = score.score( seq1[x], seq2[y])
    return S
