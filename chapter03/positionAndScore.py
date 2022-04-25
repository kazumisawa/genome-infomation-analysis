import numpy as np
def reverseLagPosition(lag,x):
    pos1 = pos2 = x
    if lag<0:
        pos2 = x - lag
    else:
        pos1 = x + lag
    return (pos1, pos2)
def positionAndScore(lag, windowScore):
    result = list()
    for x in windowScore:
        s1, s2 = reverseLagPosition(lag, x[0])
        e1, e2 = reverseLagPosition(lag, x[1])
        result.append( ( (s1+e1)/2, (s2+e2)/2, x[2] ) )
    return result
