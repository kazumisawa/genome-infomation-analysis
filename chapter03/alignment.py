import sys
from Bio import SeqIO
import scoreMatrix
import needlemanWunsch
import putGap
import fastaOutput as fa

data = list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    data.append(seq_record)
seq1, seq2  = data[0].seq, data[1].seq
range1, range2 = ( 0, len(seq1) ), ( 0, len(seq2) )
gapPenalty = 1
S = scoreMatrix.scoreMatrix(seq1, range1, seq2, range2)
path1, path2 =  needlemanWunsch.NeedlemanWunsch70(S, gapPenalty)
fa.fastaOutput( data[0].description, putGap.putGap( seq1, path1 ) )
fa.fastaOutput( data[1].description, putGap.putGap( seq2, path2 ) )
