import sys
from Bio import SeqIO
import kmer
import pair
import graphNode
import pair2deBruijn
import connect
import putOrder
import deBruijnGraph
import wordlist2seq
import time

wordLength = 5

kmerList = list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    seq = seq_record.seq.upper()
    countEach = kmer.count(wordLength+1, seq)
    kmerList.append(countEach)

pairAll = pair.pairList(kmerList)
treeAll = pair2deBruijn.node2graph(pairAll)
graphs = connect.connectedComponents(pairAll, treeAll)

wordList, resultList = list(), list()
for g in graphs:
    putOrder.putOrder(g)
    g[0].DFSlowlink()
    g[0].Fleury(wordList)
    resultList.append( wordlist2seq.wordlist2seq(wordList) )

for i in range( len(resultList) ):
    print(">" + str(i) )
    print(resultList[i])
