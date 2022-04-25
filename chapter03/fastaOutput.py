import io
import sys
from Bio import SeqIO

def fastaOutput(title, sequence):
    output = io.StringIO()
    print(">" + title, file=output)
    print(sequence, file=output)
    data = SeqIO.read( io.StringIO(output.getvalue()), "fasta")
    SeqIO.write(data, sys.stdout, "fasta")
