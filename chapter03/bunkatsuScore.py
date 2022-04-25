import numpy as np
import numpy as np
def bunkatsuScore(a, data):
    result = []
    for x in a:
        score = 0
        for i in range(x[0], x[1]):
            score += data[i]
        result.append( (x[0], x[1], score) )
    return result
