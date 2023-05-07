import sys
from Bio import Phylo
tree = Phylo.read(sys.argv[1], "newick")
Phylo.draw_ascii(tree)
