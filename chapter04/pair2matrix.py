import kmerDistance
from Bio.Phylo.TreeConstruction import DistanceMatrix

def pair2matrix(name, kmerDict):
    matrix = list()
    for i in range(len(name)):
        tmp = list()
        for j in range(i+1):
             x = kmerDict[ name[i] ]
             y = kmerDict[ name[j] ]
             tmp.append (kmerDistance.kmerDistance( y, x ) )
        matrix.append(tmp)
    return DistanceMatrix(name, matrix)
