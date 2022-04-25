import numpy as np
def normalize(org):
    mean, std = np.mean(org), np.std(org)
    return (org - mean)/std
def convert(seq, table):
    l = len(seq)
    result = np.empty( l )
    for i in range(l):
        result[i] = table[seq[i]]
    return normalize(result)
def convertPV(seq, p, v):
    p0 = convert(seq,p)
    v0 =  convert(seq,v)
    return ( p0, v0 )
