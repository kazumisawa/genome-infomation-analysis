import sys
import time

from Bio import Phylo
from Bio import SeqIO
import readVectors
import tree2pair
import pair2tree
import groupMAFFT


a,b = readVectors.readVectors(sys.argv[1])

dataDict = dict()
for seq_record in SeqIO.parse(sys.argv[2],"fasta"):
    dataDict[seq_record.id] =  seq_record.seq 

tree = Phylo.read(sys.argv[3], "newick")
internal = tree.get_nonterminals()
for i in range(len(internal)):
    internal[i].name = "internal" + str(i)

pair = tree2pair.tree2pair(tree)
root = pair2tree.pair2tree( pair, dataDict )
tmp = root[0].alignment(a,b)
root[0].show()
