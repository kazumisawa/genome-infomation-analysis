from io import StringIO
import sys
from Bio import AlignIO
from Bio.Align.Applications import MafftCommandline

mafft_exe = "mafft"
infile = sys.argv[1]
mafft_cline = MafftCommandline(mafft_exe, input = infile)
output1, output2 = mafft_cline()
align = AlignIO.read(StringIO(output1), "fasta")
