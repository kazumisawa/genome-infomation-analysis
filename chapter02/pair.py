def pairList(kmerList):
    result = list()
    for kmerCount in kmerList:
        for word in kmerCount.keys():
            result.append( (word[:-1], word[1:]) )
    return result
