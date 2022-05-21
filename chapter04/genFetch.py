import sys
from Bio import Entrez
from Bio import SeqIO
Entrez.email = sys.argv[1]
database = sys.argv[2]
handle = sys.stdin
for line in handle:
    target = ",".join(line.split())
    with Entrez.efetch(db=database,
            id=target, rettype="gb",
            retmode="text") as genbank:
        getData = genbank.readlines()
    for i in getData:
        print(i.rstrip())
