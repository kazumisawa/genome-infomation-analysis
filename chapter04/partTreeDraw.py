import sys
from Bio import SeqIO
import kmer
import recursiveTree
import internalNode

wordSize = int(sys.argv[1])
subsetSize = int(sys.argv[2])
name, title, seq = list(), dict(), dict()

for i in SeqIO.parse(sys.argv[3], "fasta"):
    name.append(i.id)
    title[i.id] = i.description
    seq[i.id] = i.seq

kmerDict = dict()
for i in name:
    kmerDict[i] = kmer.count(wordSize, seq[i])
result = recursiveTree.recursiveTree(name, seq, 
        kmerDict, subsetSize, 0)
print(type(result))
print(result.nodeNewick())
