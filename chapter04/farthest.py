import kmerDistance

def ID(OTUset, target, kmerDict):
    maxDistance, result = 0, None
    x = kmerDict[target]
    for i in OTUset:
        y = kmerDict[i]
        d = kmerDistance.kmerDistance(x,y)
        if maxDistance < d:
            maxDistance = d
            result = i
    return result
