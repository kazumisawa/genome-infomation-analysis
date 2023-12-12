import numpy as np

def peak(corr, top=20): 
    # スコアが高い順にピークを返す
    # ピークの数が多い時は上位20を返す
    dataLen = len(corr)
    if dataLen < top:
        top = dataLen #
    corrReal = np.real(corr)
    reverseOrder = np.argsort(corrReal)
    top20 = reverseOrder[:-top-1:-1]
    for i in range(top-1):
        if top20[i] > dataLen/2:
            top20[i] -= dataLen
    return top20
