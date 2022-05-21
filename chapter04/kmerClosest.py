import kmerDistance

def group(name, representers, maxLen, seq, kmerDict):
    result = dict()
    for i in representers:
        result[i] = list()
    for j in name:
        x, target = kmerDict[j], None
        minDistance = len(seq[j])+maxLen
        for i in representers:
            y = kmerDict[i]
            d = kmerDistance.kmerDistance(x,y)
            if minDistance > d:
                minDistance = d
                target = i
        result[target].append(j)
    return result
