import sys
import matplotlib.pyplot as fm
from Bio import Phylo
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

aln = AlignIO.read(sys.argv[1],"fasta")
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
constructor = DistanceTreeConstructor()
tree = constructor.upgma(dm)
tree.root_at_midpoint()

fm.rcParams['font.family'] = 'AppleGothic'
fm.rcParams["font.size"] = 12
Phylo.draw(tree)

