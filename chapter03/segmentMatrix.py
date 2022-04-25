import numpy as np
import xlist
import inverse
def segmentMatrix(tuples):
    c,d =  xlist.xlist(tuples)
    c1 = inverse.inverse(np.argsort(c))
    d1 = inverse.inverse(np.argsort(d))
    pos1, pos2 = np.zeros( len(c1) ), np.zeros( len(d1) )
    newMatrix = np.zeros( ( len(c1),len(d1) ) )
    for i in range( len(tuples) ):
        c2,d2 = int(c1[i]), int(d1[i])
        pos1[c2] = tuples[i][0]
        pos2[d2] = tuples[i][1]
        newMatrix[ c2,d2 ] = tuples[i][2]
    return list(pos1), list(pos2), newMatrix
