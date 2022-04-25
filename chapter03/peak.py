import numpy as np

def peak(corr, top=20):
    dataLen = len(corr)
    corrReal = np.real(corr)
    reverseOrder = np.argsort(corrReal)
    top20 = reverseOrder[:-top-1:-1]
    for i in range(top-1):
        if top20[i] > dataLen/2:
            top20[i] -= dataLen
    return top20
