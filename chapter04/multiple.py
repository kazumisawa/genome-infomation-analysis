import sys
from Bio import SeqIO
import groupMatrix as gm
import needlemanWunsch as nw
import putGroupGap as pg
import os
sys.path.append("/home/misawa/scripts/textbook2022/chapter03/")

seq, id = list(), list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    seq.append(seq_record.seq)
    id.append(seq_record.id)

reference = list()
reference.append( seq[0] )

for i in range(1, len(seq)):
    target = list()
    target.append(seq[i])
    r1 = ( 0, len(reference[0]) )
    r2 = ( 0, len(target[0]) )
    print(i)
    S = gm.groupMatrix(reference, r1, target, r2)
    path1, path2 =  nw.NeedlemanWunsch70(S, 1)
    reference = pg.putGroupGap(reference, path1)
    tmp = pg.putGroupGap(target, path2)
    for i in tmp:
        reference.append(i)

for i in reference:
    print(i)
