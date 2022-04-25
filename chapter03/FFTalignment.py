from Bio import SeqIO
import sys
import os
import readVectors
import putGap
import convert
import correlation2D as c2
import candidateRegions as ca
import peak
import FFTblock
import nestedAlignment as ne
import fastaOutput as fa

a,b = readVectors.readVectors(sys.argv[1])
data = list()
for seq_record in SeqIO.parse(sys.argv[2],"fasta"):
    data.append(seq_record)
seq1, seq2 = data[0].seq, data[1].seq
pv1 = convert.convertPV(seq1, a, b)
pv2 = convert.convertPV(seq2, a, b)
cr = c2.correlationPV(pv1, pv2)
corrPeak = peak.peak( cr )
region = ca.regions(corrPeak , pv1, pv2)
range1, range2 = FFTblock.FFTblock(region, len(pv1[0]), len(pv2[0]))
path1, path2 = ne.nestedAlignment(seq1, range1, seq2, range2, 1,1)
fa.fastaOutput( data[0].description, putGap.putGap( seq1, path1 ) )
fa.fastaOutput( data[1].description, putGap.putGap( seq2, path2 ) )
