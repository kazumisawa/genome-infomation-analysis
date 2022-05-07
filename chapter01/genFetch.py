import sys
from Bio import Entrez
Entrez.email = sys.argv[1]
database = sys.argv[2]
target = sys.argv[3]
with Entrez.efetch(db=database,
    id=target, rettype="gb",
    retmode="text") as genbank:
    getData = genbank.readlines()
for i in getData:
    print(i.rstrip())
