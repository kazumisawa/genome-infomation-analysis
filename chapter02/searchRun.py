import sys
from Bio import SeqIO
import BWT
import C
import Occ
import search
import subset

data = list()
for seq_record in SeqIO.parse(sys.argv[1],"fasta"):
    data.append( str(seq_record.seq).strip() )

for org in data:
    seq = org
    bwted = BWT.burrowsWheelerTransform(seq)

Occ, count =  Occ.Occ(bwted)
C = C.C(bwted,count)
query = "AAT"
if subset.isSubset(query, count):
    result = search.search(query, C, Occ, count)
else:
    result = False
