import sys
from Bio import Entrez
Entrez.email, database, target = sys.argv[1], sys.argv[2], sys.argv[3]
with Entrez.efetch(db=database, id=target, rettype="fasta",
        retmode="text") as gb:
    getData = gb.readlines()
for i in getData:
    print(i.rstrip())
