import sys
import re
from Bio import SeqIO
acc = list()
handle = sys.stdin
for seq_record in SeqIO.parse(handle, "fasta"):
    tmp = seq_record.description
    match = re.search(sys.argv[1],tmp)
    if match:
        SeqIO.write(seq_record, sys.stdout, "fasta")