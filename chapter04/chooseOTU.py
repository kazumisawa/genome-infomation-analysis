import longest
import farthest
import random

def choose(OTUlist, sequenceDict, kmerDict, subsetSize):
    first = longest.ID(OTUlist, sequenceDict)
    second = farthest.ID(OTUlist, first, kmerDict)
    subset = random.sample(OTUlist, subsetSize-2)
    subset.append(first)
    subset.append(second)
    return list(set(subset)), len(sequenceDict[first])
