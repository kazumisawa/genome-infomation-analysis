import sys
from Bio import Seq
from Bio import SeqIO

for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    print( seq_record.seq.find(sys.argv[2]) )
