import numpy as np
import convert as cv
import correlation

def norm(org): #平均0, 分散1に
    mean, std = np.mean(org), np.std(org)
    return (org - mean)/std

def groupPV(seqList, p, v):
    plist, vlist = list(), list()
    for seq in seqList:
        plist.append( cv.convert(seq, p) )
        vlist.append( cv.convert(seq, v) )
    p = norm( np.mean( np.array(plist), axis=0) )
    v = norm( np.mean( np.array(vlist), axis=0) )
    return (p, v)
