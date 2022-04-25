import matplotlib.font_manager as fm
from io import StringIO
from Bio import Phylo
fm.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams["font.size"] = 18
data = StringIO("(鮫, (鯉,鮒), (鯨,鰐));")
tree = Phylo.read(data, "newick")
Phylo.draw(tree)
