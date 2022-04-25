def SA( LF ):
    result = list()
    for i in range(len(LF)):
        j, result = 0, list()
    for i in range(len(LF)):
        j = LF[j]
        result.append(j)
    result.reverse()
    suffixArray = [0]*len(LF)
    for i in range(len(LF)):
        suffixArray[ result[i] ] = i
    return suffixArray
