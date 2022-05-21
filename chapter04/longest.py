def ID(OTUset, sequenceDict):
    maxLen, result = 0, None
    for i in OTUset:
        length = len(sequenceDict[i])
        if maxLen < length:
            maxLen = length
            result = i
    return result
