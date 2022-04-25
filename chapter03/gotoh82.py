import numpy as np
import scoreMatrix
import affineGapMatchMatrix as am
import traceBack

def gotoh82(score, w, u):
    F,P,Q = am.affineGapMatchMatrix(score, w, u)
    path1, path2 = traceBack.traceBack(F)
    result1, result2 = list(), list()
    for i in range(len(path1)-1):
        result1.append( path1[i]-1 )
        result2.append( path2[i]-1 )
    return result1, result2
