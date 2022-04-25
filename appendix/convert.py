import sys
import io
from Bio import Phylo
from Bio import SeqIO
from Bio import AlignIO
aln = AlignIO.read(sys.argv[1],"fasta")
output = io.StringIO()
for tag in aln:
    print(">" + tag.description, file=output)
    print(tag.seq, file=output)
data = AlignIO.read( io.StringIO(output.getvalue()), "fasta")
for i in data:
    print(i.description)