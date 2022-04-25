import sys
from Bio import SeqIO
import scoreMatrix
import needlemanWunsch
import gotoh82
import putGap
import fastaOutput as fa

data = list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    data.append(seq_record)
seq1, seq2  = data[0].seq, data[1].seq
range1, range2 = ( 0, len(seq1) ), ( 0, len(seq2) )
S = scoreMatrix.scoreMatrix(seq1, range1, seq2, range2)
path1, path2 =  gotoh82.gotoh82(S, 0.5, 0.5)
fa.fastaOutput( data[0].description, putGap.putGap( seq1, path1 ) )
fa.fastaOutput( data[1].description, putGap.putGap( seq2, path2 ) )
#nuc    ts      tv1     tv2
A       1       1       1
G       1       -1      -1
T       -1      1       -1
C       -1      -1      1
#AA     p       v       c
A       8.1     31      0
C       5.5     55      2.75
D       13      54      1.38
E       12.3    83      0.92
F       5.2     132     0
G       9       3       0.74
H       10.4    96      0.58
I       5.2     111     0
K       11.3    119     0.33
L       4.9     111     0
M       5.7     105     0
N       11.6    56      1.33
P       8       32.5    0.39
Q       10.5    85      0.89
R       10.5    124     0.65
S       9.2     32      1.42
T       8.6     61      0.71
V       5.9     84      0
W       5.4     170     0.13
Y       6.2     136     0.2
