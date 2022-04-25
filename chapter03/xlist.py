import numpy as np
def xlist(tuples):
    result1, result2 = [], []
    for x in tuples:
        result1.append(x[0])
        result2.append(x[1])
    return np.array(result1), np.array(result2)
