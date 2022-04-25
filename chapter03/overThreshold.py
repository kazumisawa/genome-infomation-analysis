import numpy as np
#import connect
def overThreshold(data, t):
    result= {}
    for i in range( len(data) ):
        if data[i] > t :
            result[i] = data[i]
    return result
