import numpy as np
import convert as cv
import correlation

def norm(org): #平均0, 分散1に
    mean, std = np.mean(org), np.std(org)
    return (org - mean)/std

def groupPV(seqList, p, v, range):
    plist, vlist = list(), list()
    start, end = range[0], range[1]
    for seq in seqList:
        partialSeq = seq[start:end]
        plist.append( cv.convert( partialSeq, p) )
        vlist.append( cv.convert( partialSeq, v) )
    p = norm( np.mean( np.array(plist), axis=0) )
    v = norm( np.mean( np.array(vlist), axis=0) )
    return (p, v)
