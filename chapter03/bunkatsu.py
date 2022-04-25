import numpy as np
def bunkatsu(z):
    result = []
    for i in z:
        s, e = i  # start and end
        sa  = e - s
        if sa <=150:
            result.append( (s, e) )
        else:
            q, mod = divmod(sa, 150)
            for i in range(q):
                result.append( (s+150*i, s+150*(i+1)) )
            result.append( (s+150*q, s+150*q +mod) )
    return result
