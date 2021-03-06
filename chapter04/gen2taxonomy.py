import sys
from Bio import Entrez
from Bio import SeqIO

Entrez.email, database = sys.argv[1], sys.argv[2]
target = ",".join(sys.argv[3:])
with Entrez.efetch(db=database, id=target,
           rettype="gb", retmode="text") as genbank:
    for record in SeqIO.parse( genbank, "genbank") :
        print( record.id, record.__dict__["annotations"]["taxonomy"])
