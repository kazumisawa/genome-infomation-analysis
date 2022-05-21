import sys
from Bio import SeqIO
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import kmer
import kmerDistance
import pair2matrix
import kmerClosest
import chooseOTU
import internalNode

def recursiveTree(OTUlist, seq, kmerDict, subsetSize, depth):
    result = internalNode.internalNode("internal" + str(depth) )
    if len(OTUlist) <= subsetSize:
        for i in OTUlist:
            leaf = internalNode.internalNode(i)
            result.addKid(leaf)
        return result
    subset, m = chooseOTU.choose(OTUlist, seq, kmerDict, subsetSize)
    newDM = pair2matrix.pair2matrix(subset,kmerDict)
    constructor = DistanceTreeConstructor()
    tree = constructor.upgma(newDM)
    groups = kmerClosest.group(OTUlist, subset, m, seq, kmerDict)
    for i in subset:
        result.addKid(recursiveTree(groups[i], seq, kmerDict, subsetSize, 
            depth+1))
    return result
