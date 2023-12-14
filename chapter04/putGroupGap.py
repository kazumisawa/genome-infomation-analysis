import putGap

def putGroupGap(orgGroup, reverse, range1): 
    # rangeで指定した領域をreverseに従いgapを入れる
    start, end = range1[0], range1[1]
    result = list()
    for i in range( len(orgGroup) ):
        result.append( putGap.putGap(orgGroup[i][start:end], reverse) )
    return result
