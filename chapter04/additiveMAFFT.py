import sys
from Bio import SeqIO
import readVectors
import groupMAFFT
import fastaOutput as fa

a,b = readVectors.readVectors(sys.argv[1])
data = list()

seq, description = list(), list()
for seq_record in SeqIO.parse(sys.argv[2],"fasta"):
    seq.append( seq_record.seq )
    description.append(seq_record.description)

mainGroup = list()
mainGroup.append( seq[0] )

for i in range(1, len(seq)):
    subGroup = list()
    subGroup.append(seq[i])
    mainGroup = groupMAFFT.groupMAFFT(mainGroup, subGroup, a, b)

for i in range(len(seq)):
    fa.fastaOutput( description[i], mainGroup[i] )
