import putGap

def putGroupGap(orgGroup, reverse): #pathをたどる
    result = list()
    for i in range( len(orgGroup) ):
        result.append( putGap.putGap(orgGroup[i], reverse) )
    return result

