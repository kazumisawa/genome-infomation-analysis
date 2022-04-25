import numpy as np
def inverse(intArray):
    l = len(intArray)
    gyaku = np.empty( l )
    for i in range( l ):
        gyaku[intArray[i]]=i
    return list(gyaku)
