import sys
from Bio.Align.Applications import ClustalwCommandline

exe = "clustalw2"
infile = sys.argv[1]
clustalw_cline = ClustalwCommandline(exe, infile = infile )
output1, output2 = clustalw_cline()
