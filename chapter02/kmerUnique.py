from __future__ import print_function

import sys
from io import StringIO
from Bio import SeqIO
# from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

target = list()
k=int(sys.argv[1])
count = dict()

for seq_record in SeqIO.parse(sys.argv[2],"fasta"):
    target.append(seq_record)

for i in range(len(target)):
    seq = str( target[i].seq )
    for j in range( len(seq)-k ):
        tag = seq[j:j+k]
        if tag in count:
            count[tag] +=1
        else:
            count[tag] = 1
            reverseTag = str(Seq(tag).reverse_complement())
            count[reverseTag] = 1

#output depending on word count
for i in range(len(target)):
    seq = str( target[i].seq )
    newSeq = list()
    for j in range( len(seq)-k ):
        tag = seq[j:j+k]
        if count[tag] ==1:
            newSeq.append( seq[j])
        else:
            newSeq.append( seq[j].lower() )
    buffer = StringIO(">" + target[i].description + "\n" + "".join(newSeq) )
    SeqIO.write( SeqIO.parse(buffer,"fasta"), sys.stdout, "fasta" )
    buffer.close()
